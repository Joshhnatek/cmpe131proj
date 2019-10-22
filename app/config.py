import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'something something' # os.environ.get('SECRET_KEY')
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///databases/app.db'
    SQALCHEMY_TRACK_MODIFICATIONS = False
