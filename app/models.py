from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login
from flask_login import UserMixin

class User(db.Model, UserMixin):
    """Contains the information on all registered users.

    Attributes:
        __tablename__ (string): Name for user database model.
        id (int): Unique ID assigned to each user.
        username (string): User's username.
        email (string): User's email address.
        password_hash (string): User's password after hashing.
    """
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))


    def __repr__(self):
        """Prints the current user's username."""
        return '{}'.format(self.username)

    def set_password(self, password):
        """Hashes user's input password and sets it.

        Args:
            password (string): The password the user inputted to the form.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Checks if the user inputted the same password

        Args:
            password (string): The second password the user inputted to the form.

        Returns:
            If passwords match, returns True. Otherwise, returns False.
        """
        return check_password_hash(self.password_hash, password)

class Pantry(db.Model):
    """Contains the information on the users' virtual pantries.

    Attributes:
        __tablename__ (string): Name for virtual pantry database model.
        id (int): ID for each user and ingredient combination.
        user_id (int): User's ID.
        ingredient_id (int): Ingredient's ID.
        ingredient_name (string): Ingredient's name.
    """
    __tablename__ = 'pantry'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, index=True)
    ingredient_id = db.Column(db.Integer, index=True)
    ingredient_name = db.Column(db.String(128), index=True)

    def __repr__(self):
        """Prints the user's ID, ingredient's ID and name."""
        return '{}:{}:{}'.format(self.user_id, self.ingredient_id, self.ingredient_name)

@login.user_loader
def load_user(id):
    """Returns the user's ID from the user database model.

    Args:
        id (int): The user's ID.

    Returns:
        If the ID is found, returns the user information from the database. Otherwise, returns None.
    """
    return User.query.get(int(id))

class Ingredients(db.Model):
    """Contains the information on all our available ingredients.

    Attributes:
        __tablename__ (string): Name for ingredient database model.
        id (int): Unique ID assigned to each ingredient.
        name (string): Ingredient's name.
        category (string): Ingredient's category name.
    """
    __tablename__ = 'ingredient'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(128), index=True)
    category = db.Column(db.String(128), index=True)

    def __repr__(self):
        """Prints the ingredient's category, name and ID."""
        return '{}:{}:{}'.format(self.category, self.name, self.id)

    def get_id(category, name):
        """Returns the ingredient's ID.

        Args:
            category (string): The ingredient's category.
            name (string): The ingredient's name.

        Returns:
            If the ingredient is found, returns the ingredient ID from the database. Otherwise, returns None.
        """
        item = Ingredients.query.filter_by(category=category).filter_by(name=name).first()
        return item.id

class recipes(db.Model):
    """Contains the information on all available recipes.

    Attributes:
        __tablename__ (string): Name for recipe database model.
        id (int): ID for each recipe.
        recipeN (string): Recipe name.
        ingredients: Relationship with recipeIng database model.
    """
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True, unique = True )
    recipeN =  db.Column(db.String(128), index = True)
    ingredients = db.relationship('recipeIng', backref='recipe')
    def __repr__(self):
        return '{}:{}'.format(self.id, self.recipeN) #might have to connect child

class recipeIng(db.Model):
    """Contains the information on .

        Attributes:
            __tablename__ (string): Name for recipe ingredient database.
            recipe_id (int): ID for each recipe.
            ingredient_id (int): Ingredient's ID.
            ingredient_ammount (int): Amount of the ingredient.
        """
    __tablename__ = 'recipeIng'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id')) #not sure if need index
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id')) #connected ingredient id just in case
    ingredient_ammount = db.Column(db.Integer, index = True)

    def __repr__(self):
        return '{}:{}:{}:{}'.format(self.id, self.recipe_id, self.ingredient_id, self.ingredient_ammount)
