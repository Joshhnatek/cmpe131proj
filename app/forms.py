from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import User, Ingredients

class User_Form(FlaskForm):
    """Contains the fields needed for the user login."""
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class Registration_Form(FlaskForm):
    """Contains the fields needed for user registration."""
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        """Checks if a username is already in the user database.

        Args:
            username(string): The username inputted by the user.

        Raises:
            ValidationError: Username is already in user database.
        """
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Username is already in use")

    def validate_email(self, email):
        """Checks if a email is already in the user database.

        Args:
            email(string): The email inputted by the user.

        Raises:
            ValidationError: Email is already in user database.
        """
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Email is already in use")

class Add_Ingredient_Form(FlaskForm):
    """Contains all the fields needed for adding ingredients."""
    category = SelectField('Category', choices= [])
    name = SelectField('Name', choices= [])
    submit = SubmitField('Add Ingredient(s)')
    confirm = SubmitField('Confirm')

class Remove_Ingredient_Form(FlaskForm):
    """Contains all the fields needed for removing ingredients."""
    pantry = SelectField('Pantry', choices=[])
    remove = SubmitField('Remove Ingredient')

