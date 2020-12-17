from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_user, logout_user, login_required, current_user

from .models import Recipe
from .forms import RecipeForm
from . import db

recipe = Blueprint('recipe', __name__)

@recipe.route('/create-recipe')
def create_recipe():
    form = RecipeForm()
    return render_template('create_recipe.jinja', form=form)

@recipe.route('/create-recipe', methods=['POST'])
def create_recipe_post():
    print('CREATE RECIPE')
    form = RecipeForm(request.form)

    # read form, create recipe DB object, add it and get id
    name = form.get('name')
    description = form.get('description')
    ingredients = form.get('ingredients')
    directions = form.get('directions')
    notes = form.get('notes')

    # current_user = User object
    #print(current_user.name)

    # new user, create, hash password
    new_recipe = Recipe(name=name, description=description, ingredients=ingredients, directions=directions, notes=notes)

    db.session.add(new_recipe)
    db.session.commit()
    print('new recipe added: ',new_recipe.id)

    #id = 1
    return redirect(url_for('recipe.browse_recipe', id=new_recipe.id))

@recipe.route('/recipe/<id>')
def browse_recipe(id):
    return(id)