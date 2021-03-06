import os

from codenames_backend import create_app
from codenames_backend.models import db
from codenames_backend.models.words import Word


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///instance/app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app = create_app(Config)

with app.app_context():
    Word.query.delete()
    with open("words.txt", "r") as f:
        for word in f:
            db.session.add(Word(word=word.strip()))
    db.session.commit()
