from flask import Flask
from flask_admin import Admin
import flask_sqlalchemy
import app.config as Configuration
from app.views import UserView, AdminView, PostView
from flask_admin.menu import MenuLink
from flask_login import LoginManager

'''
    Instantiare DB and Login Manager
'''
db = flask_sqlalchemy.SQLAlchemy()
login = LoginManager()


def create_app():

    """
        Create App
    """
    app = Flask(__name__)

    '''
        Init Database
    '''
    db.init_app(app)

    '''
        Init Login
    '''
    login.init_app(app)
    '''
        Configuring App
    '''
    Configuration.config(app)

    '''
        Administration interface
    '''
    from app.models import User, Post
    # Admin Left Side
    admin = Admin(app, index_view=AdminView(url='/admin'), template_mode='bootstrap3')
    admin.add_view(UserView(User, db.session))
    admin.add_view(PostView(Post, db.session))
    # Admin Right Side
    admin.add_link(MenuLink(name='Torna al sito publico', endpoint='public.public'))

    '''
        Add Blueprint Routes
    '''
    from app.routes import register_blueprints_routes
    register_blueprints_routes(app)

    '''
        Return Configured App
    '''
    return app




