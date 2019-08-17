import psycopg2

def config(app):
    # set optional bootswatch theme
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    DB_URL = 'postgresql+psycopg2://admin:admin@localhost:5432/dbrizzi'
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'