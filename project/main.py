# system imports

# 3rd party imports
from flask import Blueprint, render_template
from flask_login import login_required, current_user

# local imports
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html.j2')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html.j2', name=current_user.name)