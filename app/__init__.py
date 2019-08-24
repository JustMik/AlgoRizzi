import os
from flask import Flask, url_for, redirect, send_from_directory
from flask_admin import Admin
import flask_sqlalchemy
import app.config as Configuration
from app.views import UserView, AdminView, PostView
from flask_admin.menu import MenuLink
from flask_login import LoginManager

#Instantiare db
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
    # Left Side
    admin = Admin(app, index_view=AdminView(url='/admin'), template_mode='bootstrap3')
    admin.add_view(UserView(User, db.session))
    admin.add_view(PostView(Post, db.session))
    # Right Side
    admin.add_link(MenuLink(name='Torna al sito publico', endpoint='public.public'))


    '''
        Add Blueprint Routes
    '''
    from app.routes import public_route, flask_security, handler_route
    #Register Routes Blueprint
    #app.register_blueprint(admin_route)
    app.register_blueprint(public_route)
    app.register_blueprint(flask_security)
    app.register_blueprint(handler_route)

    '''
        Markdown
    '''
    from flask_misaka import Misaka
    markdown = Misaka()
    markdown.init_app(app)

    '''
        Redirect '/' to '/public'
    '''
    @app.route('/')
    def index():
        return redirect(url_for('public.public'))

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

    '''
        Return Configured App
    '''
    return app




