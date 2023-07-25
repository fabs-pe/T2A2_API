from init import db, ma 
from marshmallow import fields

class Song(db.Model):
    __tablename__ = 'songs'

    id =db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)

    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
    # playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'), nullable=False)
    
    artist = db.relationship('Artist', back_populates='songs')
    songlists = db.relationship('Songlist', back_populates='song')