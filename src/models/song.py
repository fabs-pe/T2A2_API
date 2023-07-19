from init import db, ma 

class Song(db.Model):
    __tablename__ = 'songs'

    id =db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.text, nullable=False)

    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)