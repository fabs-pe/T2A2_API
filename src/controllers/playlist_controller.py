from flask import Blueprint, request
from init import db
from models.playlist import Playlist, playlists_schema, playlist_schema

playlists_bp = Blueprint('playlists', __name__, url_prefix='/playlists')

@playlists_bp.route('/')
def get_all_playlists():
    stmt = db.select(Playlist).order_by(Playlist.date_created.desc())
    playlists = db.session.scalars(stmt)
    return playlists_schema.dump(playlists)

@playlists_bp.route('/<int:id>')
def get_one_playlist(id):
    stmt = db.select(Playlist).filter_by(id=id)
    playlist = db.session.scalar(stmt)
    if playlist:
        return playlist_schema.dump(playlist)
    else:
        return {'error': f'Playlist not found with id {id}'}, 404