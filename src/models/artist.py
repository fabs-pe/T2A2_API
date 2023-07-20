from init import db, ma

class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(50))
    country = db.Column(db.String(50))

    