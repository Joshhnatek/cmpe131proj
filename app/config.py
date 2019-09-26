import os
basedir = os.path.abspath(os.path.dirname(__file__name))

class Config(object):
    SQALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQALCHEMY_TRACK_MODIFICATIONS = False