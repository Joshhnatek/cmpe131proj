from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField

class ingredient_form(FlaskForm):
    
    # "Add Ingredient" - Button
    # On click..interface to select:
    # Category of ingredient
    # Name
    # Quantity
    # Confirm button