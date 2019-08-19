from flask import Flask, url_for, redirect
from flask_admin import Admin
import flask_sqlalchemy
import app.config as Configuration
from app.models.users import User
from flask_security import Security
from app.views.Test1 import Test1
from app.views.Test2 import Test2
from flask_admin.contrib.sqla import ModelView
from flask_bootstrap import Bootstrap
from flask_admin.menu import MenuLink
from app.routes.public import public_route
from app.routes.security import flask_security
from app.routes.handler import handler_route


app = Flask(__name__)

#Security
security = Security()


#Instantiare db
db = flask_sqlalchemy.SQLAlchemy(app)
Configuration.config(app)

#Add Bootstrap
Bootstrap(app)

#Register Routes Blueprint
#app.register_blueprint(admin_route)
app.register_blueprint(public_route)
app.register_blueprint(flask_security)
app.register_blueprint(handler_route)
security.init_app(app)

#Administration interface
admin = Admin(app, name='admin', template_mode='bootstrap3')
admin.add_view(Test1(name='Hello 1', endpoint='test1', category='Test'))
admin.add_view(Test2(name='Hello 2', endpoint='test2', category='Test'))
admin.add_view(ModelView(User, db.session))
admin.add_link(MenuLink(name='Torna al sito publico', endpoint='public.public'))


@app.route('/')
def index():
    return redirect(url_for('public.public'))



