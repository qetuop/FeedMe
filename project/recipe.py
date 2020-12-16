from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_user, logout_user, login_required, current_user

from . import db

recipe = Blueprint('recipe', __name__)

@recipe.route('/create-recipe')
def create_recipe():
    # current_user = User object
    #print(current_user.name)
    return render_template('create_recipe.jinja')