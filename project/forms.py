from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, FileField, TextAreaField, TextField

class Recipe(FlaskForm):
    name = TextField('Name')
    ingredients = TextAreaField('Ingredients')