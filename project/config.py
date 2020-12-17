import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'igottasetsomething'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False