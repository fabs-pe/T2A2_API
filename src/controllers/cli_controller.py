from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.playlist import Playlist
# from models.song import Song
# from models.artist import Artist
from datetime import date

db_commands = Blueprint('db', __name__)

@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Tables Created")

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command('seed')
def seed_db():
    users =[
        User(
            name= 'admin',
            email='admin@theboss.com',
            password=bcrypt.generate_password_hash('admin2417').decode('utf-8'),
            is_admin=True
        ),
        User(
            name='John Smith',
            email='johns@company.com',
            password=bcrypt.generate_password_hash('password12').decode('utf-8')
        ),
        User(
            name='Biance Jones',
            email= 'biance@company.com',
            password=bcrypt.generate_password_hash('password12').decode('utf-8')
        ),
        User(
            name ='Sally Turner',
            email='sally@company.com',
            password=bcrypt.generate_password_hash('password12').decode('utf-8')

        ),
        User(
            name= 'Scott User',
            email= 'scott@mail.com',
            password= bcrypt.generate_password_hash('pasword12').decode('utf-8')
        )
    ]

    db.session.add_all(users)

    playlists =[
        Playlist(
            title='Work',
            date_created = date.today(),
            description= 'Work Safe Music',
            user =users[0]
        ),
        Playlist(
            title = 'Pre-drinks',
            date_created = date.today(),
            description = 'Get me pumped',
            user = users[0]
        ),
        Playlist(
            title= 'Gym',
            date_created= date.today(),
            user =users[0]
        ),
        Playlist(
            title = 'Sleep',
            date_created= date.today(),
            user =users[0]
        ),
        Playlist(
            title = '40th Party',
            date_created = date.today(),
            description = 'Scotts Favourites',
            user =users[0]
        ),
        Playlist(
            title = '70s',
            date_created = date.today(),
            user = users[0]
        ),
        Playlist(
            title = 'Todays Hits',
            date_created = date.today(),
            description = 'Latets and Best',
            user = users[0]
        ),
        Playlist(
            title = 'Road Trip',
            date_created = date.today(),
            description = 'Sing along fun',
            user = users[0] 
        )
    ]


    db.session.add_all(playlists)
    db.session.commit()


    print("Tables seeded")