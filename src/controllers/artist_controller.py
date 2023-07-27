from flask import Blueprint, request
from init import db
from models.artist import Artist, artist_schema, artists_schema
from flask_jwt_extended import get_jwt_identity, jwt_required

artists_bp = Blueprint('artists', __name__, url_prefix = '/artists')

@artists_bp.route('/', methods =['GET'])
def get_all_artists():
    stmt = db.select(Artist)
    artists =db.session.scalars(stmt)
    return artists_schema.dump(artists)

@artists_bp.route('/<int:id>', methods =['GET'])
def get_one_artist(id):
    stmt = db.select(Artist).filter_by(id=id)
    artist = db.session.scalar(stmt)
    if artist:
        return artist_schema.dump(artist)
    else:
        return{'error': f'Artist with id {id} not found'}
    
@artists_bp.route('/', methods = ['POST'])
@jwt_required()
def create_artist():
    body_data = request.get_json()
    artist = Artist(
        artist_name = body_data.get('artist_name'),
        country = body_data.get('country'),
    )
    db.session.add(artist)
    db.session.commit()

    return artist_schema.dump(artist), 201

@artists_bp.route('/<int:id>', methods =['DELETE'])
@jwt_required()
def delete_one_artist(id):
    stmt =db.select(Artist). filter_by(id=id)
    artist = db.session.scalar(stmt)
    if artist:
        db.session.delete(artist)
        db.session.commit()
        return {'message': f'{artist.artist_name} has been deleted successfully'}
    else:
        return {'error' : f'Artist not found with id {id}'}, 404
    