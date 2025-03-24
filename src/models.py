from . import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    studio = db.Column(db.String(100), nullable=False)
    ratings = db.Column(db.Integer, nullable=False)
    platforms = db.Column(db.ARRAY(db.String), nullable=False)

    def __repr__(self):
        return f'<Game {self.name}>'
