from init import db, ma
from marshmallow import fields

class Songlist(db.Model):
    __tablename__ = 'songlists'

    id = db.Column(db.Integer, primary_key=True)

    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'), nullable=False)

    song = db.relationship('Song', back_populates='songlists')
    playlist = db.relationship('Playlist', back_populates='songlists')

class SonglistSchema(ma.Schema):
    playlist = fields.Nested('PlaylistSchema', only = ['id','title', 'description']) # joins 
    song = fields.Nested('SongSchema', only = ['title', 'genre'])
    
    class Meta:
        fields = ('id','playlist', 'song')
        ordered = True

songlist_schema = SonglistSchema()
songlists_schema = SonglistSchema(many=True)