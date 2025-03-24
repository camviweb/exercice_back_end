from .models import Game
from . import db
from datetime import datetime

def init_db():
    db.create_all()
    data()

def data():
    if Game.query.count() == 0:
        games = [
            Game(
                name="The Witcher 3 : Wild Hunt",
                release_date=datetime.strptime("2015-05-19", "%Y-%m-%d"),
                studio="CD Projekt RED",
                ratings=19,
                platforms=["PC", "PS4", "PS5", "Switch", "One"]
            ),
            Game(
                name="Mario Kart 8 Deluxe",
                release_date=datetime.strptime("2017-04-28", "%Y-%m-%d"),
                studio="Nintendo",
                ratings=16,
                platforms=["Switch"]
            ),
            Game(
                name="Don't Starve",
                release_date=datetime.strptime("2013-04-23", "%Y-%m-%d"),
                studio="Capybara Games",
                ratings=17,
                platforms=["PC", "PS4", "Switch", "One", "WiiU", "PS3"]
            )
        ]
        db.session.bulk_save_objects(games)
        db.session.commit()
