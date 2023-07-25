from flask import Blueprint, request
from init import db
from models.song import Song, songs_schema, song_schema

songs_bp = Blueprint('songs', __name__, url_prefix='/songs')

@songs_bp.route('/', methods =['GET'])
def get_all_songs():
    stmt = db.select(Song).order_by(Song.genre.desc())
    songs = db.session.scalars(stmt)
    return songs_schema.dump(songs)

@songs_bp.route('/<int:id>', methods =['GET'])
def get_one_song(id):
    stmt = db.select(Song).filter_by(id=id)
    song = db.session.scalar(stmt)
    if song:
        return song_schema.dump(song)
    else:
        return {'error': f'Song not found with id {id}'}, 404