from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = Config.SECRET_KEY

login = LoginManager(app)
login.login_view = 'login'

db = SQLAlchemy(app)

from app import routes, models, forms

