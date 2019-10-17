import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    
    SQALCHEMY_DATABASE_URI = 'sqlite:////~/CMPE131/Project/cmpe131proj/app/databases'
    SQALCHEMY_TRACK_MODIFICATIONS = False