import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'something something'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///databases/app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False