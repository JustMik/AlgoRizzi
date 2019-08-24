import psycopg2
from flask_bootstrap import Bootstrap
from flask import session
from datetime import timedelta

SESSION_TIMEOUT = 300  #minuti
ADMIN_TEMPLATE = 'cerulean'
DB_URL = 'postgresql+psycopg2://admin:admin@localhost:5432/dbrizzi'
SECRET_KEY = 'super secret key'

def config(app):
    # set optional bootswatch theme
    app.config['FLASK_ADMIN_SWATCH'] = ADMIN_TEMPLATE
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
    app.secret_key = SECRET_KEY
    app.config['SESSION_TYPE'] = 'filesystem'
    Bootstrap(app)

    @app.before_request
    def before_request():
        session.permanent = True
        app.permanent_session_lifetime = timedelta(seconds=SESSION_TIMEOUT)


