from flask import Blueprint, request
from init import db
from models.playlist import Playlist, playlists_schema, playlist_schema
from models.song_list import Songlist, SonglistSchema
from datetime import date
from flask_jwt_extended import get_jwt_identity, jwt_required

playlists_bp = Blueprint('playlists', __name__, url_prefix='/playlists')

@playlists_bp.route('/', methods =['GET'])
def get_all_playlists():
    stmt = db.select(Playlist).order_by(Playlist.date_created.desc())
    playlists = db.session.scalars(stmt)
    return playlists_schema.dump(playlists)

@playlists_bp.route('/<int:id>', methods =['GET'])
def get_one_playlist(id):
    stmt = db.select(Playlist).filter_by(id=id)
    playlist = db.session.scalar(stmt)
    if playlist:
        return playlist_schema.dump(playlist)
    else:
        return {'error': f'Playlist not found with id {id}'}, 404
    
@playlists_bp.route('/', methods = ['POST'])
@jwt_required()
def create_playlist():
    body_data = request.get_json()
    playlist = Playlist(
        user_id = get_jwt_identity(),
        title = body_data.get('title'),
        description = body_data.get('description'),
        date_created = date.today()
    )
    db.session.add(playlist)
    db.session.commit()

    return playlist_schema.dump(playlist), 201

@playlists_bp.route('/<int:id>', methods =['DELETE'])
@jwt_required()
def delete_one_playlist(id):
    stmt =db.select(Playlist). filter_by(id=id)
    playlist = db.session.scalar(stmt)
    if playlist:
        db.session.delete(playlist)
        db.session.commit()
        return {'message': f'Playlist {playlist.title} deleted successfully'}
    else:
        return {'error' : f'Playlist not found with id{id}'}, 404
    