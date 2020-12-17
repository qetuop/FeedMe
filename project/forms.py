from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, FileField, TextAreaField, TextField
from wtforms.validators import DataRequired, Length

class RecipeForm(FlaskForm):
    name = TextField('Recipe Name', [DataRequired(), Length(min=1, message=('Your Name is too short.'))])
    description = TextAreaField('Desription', [DataRequired(), Length(min=1, message=('Your Description is too short.'))])
    ingredients = TextAreaField('Ingredients', [DataRequired(), Length(min=1, message=('Add at least 1 ingredient.'))])
    directions = TextAreaField('Directions', [DataRequired(), Length(min=1, message=('Add at least 1 step.'))])
    notes = TextAreaField('Notes')

    save = SubmitField('Save')
    cancel = SubmitField('Cancel')
    