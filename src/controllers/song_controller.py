from flask import Blueprint, request
from init import db
from models.song import Song, songs_schema, song_schema
from models.artist import Artist, artist_schema, artists_schema
from flask_jwt_extended import get_jwt_identity, jwt_required

songs_bp = Blueprint('songs', __name__, url_prefix='/songs')

# Get all songs
@songs_bp.route('/', methods =['GET'])
def get_all_songs():
    stmt = db.select(Song).order_by(Song.genre.desc())
    songs = db.session.scalars(stmt)
    return songs_schema.dump(songs)

# Get one song by using id
@songs_bp.route('/<int:id>', methods =['GET']) 
def get_one_song(id):
    stmt = db.select(Song).filter_by(id=id)
    song = db.session.scalar(stmt)
    if song:
        return song_schema.dump(song)  # display song with matching id
    else:
        return {'error': f'Song not found with id {id}'}, 404  # catch error if id is not found
    
# Create new Song Model Instance
@songs_bp.route('/', methods = ['POST'])
@jwt_required()
def create_song():
    body_data = request.get_json()
    song = Song(
        artist_id = get_jwt_identity(),
        genre = body_data.get('genre'),
        title = body_data.get('title'),
    )
    db.session.add(song) 
    db.session.commit()

    return song_schema.dump(song), 201

# Delete a single song
@songs_bp.route('/<int:id>', methods =['DELETE']) # the id of song to be deleted
@jwt_required()
def delete_one_songs(id):
    stmt =db.select(Song). filter_by(id=id)
    song = db.session.scalar(stmt)
    if song:
        db.session.delete(song)
        db.session.commit()
        return {'message': f'Song {song.title} deleted successfully'} # Confirm that song was deleted successfully
    else:
        return {'error' : f'Song not found with id {id}'}, 404 # let user know the id doesnt exist
    
@songs_bp.route('/<int:id>', methods = ['PUT', 'PATCH'])
@jwt_required()
def update_one_song(id):
    body_data = request.get_json()
    stmt = db.select(Song).filter_by(id =id)
    song = db.session.scalar(stmt)
    if song:
        song.title = body_data.get('title') or song.title
        song.genre = body_data.get('genre') or song.genre
        db.session.commit()
        return song_schema.dump(song)
    
    else: 
        return {'error' : f'Song with id {id} not found'}, 404
