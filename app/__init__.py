from flask import Flask
from app.config import Config
from app.ingredients_list import meats, spices, carbohydrates, vegetables, fruits
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
#from flask_heroku import Heroku

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = Config.SECRET_KEY

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

#heroku = Heroku()


def create_app(test_config = None):
    app = Flask(__name__, instance_relative_config= False)
    
    if test_config is None:
        app.config.from_object(Config)
        app.config['SECRET_KEY'] = Config.SECRET_KEY
    else: 
        app.config.from_mapping(test_config)

    db.init_app(app)
    login.init_app(app)
    login.login_view = 'login'
    

    with app.app_context():
        from . import routes
        db.create_all()
        return app



@app.before_first_request
def create_tables():
    from app.models import User, Ingredients, Pantry, recipes, recipeIng
    db.create_all()

from app import routes, models, forms

