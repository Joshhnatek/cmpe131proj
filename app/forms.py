from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField

class User_Form(FlaskForm):
    email = StringField('Email')
    password = PasswordField('Password')
    remember = BooleanField('Keep Me Logged In')
    submit = SubmitField('Login')