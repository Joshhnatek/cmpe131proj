from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))


    def __repr__(self):
        return '{}'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Pantry(db.Model):
    __tablename__ = 'pantry'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, index=True)
    ingredient_id = db.Column(db.Integer, index=True)
    ingredient_name = db.Column(db.String(128), index=True)

    def __repr__(self):
        return '{}:{}:{}'.format(self.user_id, self.ingredient_id, self.ingredient_name)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Ingredients(db.Model):
    __tablename__ = 'ingredient'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(128), index=True)
    category = db.Column(db.String(128), index=True)

    def __repr__(self):
        return '{}:{}:{}'.format(self.category, self.name, self.id)

    def get_id(self, category, name):
        item = Ingredients.query.filter_by(category='category').filter_by(name='name').first()
        return item.id

class recipes(db.model):
    __tablename__ = 'recipes'
    recipeid = db.Column(db.Integer, primary_key=True, unique = True )
    recipeN =  db.Column(db.String(128), index = True)
    #recipeI = db.Column()

    def __repr__(self):
        return '{}:{}'.format(self.recipeid, self.recipeN) #might have to connect child

class recipeIng(db.model):
    __tablename__ = 'recipeIng'
    recipe_id = Column(db.Integer, db.ForeignKey('recipes.recipeid')) #not sure if need index
    recipe_ingr = (db.String(128), index =True, primary_key = True)
    recipe_id = (db.Integer, db.ForeignKey('Ingredients.id')) #connected ingredient id just in case
    recipe_amount = (db.Integer, index = True)

    def __repr__(self):
        return '{}:{}:{}:{}'.format(self.recipe_id, self.recipe_ingr, self.recipe_id, self.recipe_amount)
