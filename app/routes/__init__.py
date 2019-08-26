from app.routes.admin import admin_route
from app.routes.public import public_route
from app.routes.security import flask_security
from app.routes.handler import handler_route
from app.routes.graph.coverage import coverage_route
from flask import url_for, redirect



def register_blueprints_routes(app):
    app.register_blueprint(public_route)
    app.register_blueprint(flask_security)
    app.register_blueprint(handler_route)
    app.register_blueprint(coverage_route)

    '''
        Redirect '/' to '/public'
    '''
    @app.route('/')
    def index():
        return redirect(url_for('public.public'))
