import psycopg2
from flask_bootstrap import Bootstrap
from flask import session, send_from_directory
from datetime import timedelta
import os

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

    '''
        Provide favicon
    '''
    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

    ''' 
        Reset session timeout before every call
    '''
    @app.before_request
    def before_request():
        session.permanent = True
        app.permanent_session_lifetime = timedelta(seconds=SESSION_TIMEOUT)

    '''
        Jinja2 Date time filter
    '''
    @app.template_filter('strftime')
    def filter_datetime(date):
        return date.strftime('%H:%M - %d/%m/%Y')


