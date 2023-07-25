from flask import Blueprint, request
from init import db
from models.song_list import Songlist, songlist_schema, songlists_schema

songlists_bp = Blueprint('songlists', __name__, url_prefix='/songlists')

@songlists_bp.route('/', methods =['GET'])
def get_all_lists():
    stmt = db.select(Songlist)
    songlists = db.session.scalars(stmt)
    return songlists_schema.dump(songlists)

@songlists_bp.route('/<int:id>', methods =['GET'])
def get_one_list(id):
    stmt = db.select(Songlist).filter_by(id=id)
    songlist = db.session.scalar(stmt)
    if songlist:
        return songlist_schema.dump(songlist)
    else:
        return {'error': f'Songlist not found with id {id}'}, 404