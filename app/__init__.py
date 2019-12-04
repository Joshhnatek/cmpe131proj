from flask import Flask
from app.config import Config
from app.ingredients_list import meats, spices, carbohydrates, vegetables, fruits
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = Config.SECRET_KEY

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

@app.before_first_request
def create_tables():
    from app.models import User, Ingredients, Pantry, recipes, recipeIng
    db.create_all()

from app import routes, models, forms

