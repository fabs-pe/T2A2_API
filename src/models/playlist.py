from init import db, ma 
from marshmallow import fields

class Playlist(db.Model):
    __tablename__ = 'playlists'

    id =db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    date_created = db.Column(db.Date) # Date created
    description = db.Column(db.String(50))
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='playlists')