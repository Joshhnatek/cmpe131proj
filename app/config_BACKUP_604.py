import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
<<<<<<< HEAD
    SECRET_KEY = 'something something'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///databases/app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
=======
    SECRET_KEY = 'something something' # os.environ.get('SECRET_KEY')
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///databases/app.db'
    SQALCHEMY_TRACK_MODIFICATIONS = False
>>>>>>> 540774116c15fd74d51dcdb2893d01bba80e0dee
