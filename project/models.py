from flask_login import UserMixin

from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    # one to many (User to Recipe)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    ingredients = db.Column(db.String(1000))
    directions = db.Column(db.String(1000))
    notes = db.Column(db.String(1000))

    # many to one  (Recipe to User)
