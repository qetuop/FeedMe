from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from .config import Config

# init SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    # link db to app
    db.init_app(app)

    # flask_login setup
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return (User.query.get(int(user_id)))

    # auth routes blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # auth routes blueprint
    from .recipe import recipe as recipe_blueprint
    app.register_blueprint(recipe_blueprint)

    # main routes blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #with app.test_request_context():
    #    print(url_for('main.index'))
    
    return app