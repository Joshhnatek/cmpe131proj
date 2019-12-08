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

    def get_users_items(users_id):
        items = Pantry.query.filter_by(user_id=users_id).all()
        return items

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

    def get_id(category, name):
        item = Ingredients.query.filter_by(category=category).filter_by(name=name).first()
        return item.id

    def get_ingredient_name(id):
        ingredient = Ingredients.query.filter_by(id = id).first()
        if(ingredient):
            return ingredient.name
        else: return None

class recipes(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True, unique = True )
    recipeN =  db.Column(db.String(128), index = True)
    ingredients = db.relationship('recipeIng', backref='recipe')
    essentialIng = db.Column(db.Integer)
    def __repr__(self):
        return '{}:{}'.format(self.id, self.recipeN) #might have to connect child

    def get_name(r_id):
        recipe = recipes.query.filter_by(id = r_id).first()
        if(recipe): 
            return recipe.name
        else: return None

class recipeIng(db.Model):
    __tablename__ = 'recipeIng'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id')) #not sure if need index
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id')) #connected ingredient id just in case
    ingredient_ammount = db.Column(db.Integer, index = True)

    def __repr__(self):
        return '{}:{}:{}:{}'.format(self.id, self.recipe_id, self.ingredient_id, self.ingredient_ammount)

    