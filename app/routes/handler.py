from flask import Blueprint, render_template, redirect,url_for

handler_route = Blueprint('handler_route',__name__)

@handler_route.app_errorhandler(404)
def page_not_found(error):
    # note that we set the 404 status explicitly
    return render_template('utils/404.html'), 404


@handler_route.app_errorhandler(403)
def page_not_found(error):
    # note that we set the 404 status explicitly
    return redirect(url_for('flask_security.login'))