from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_user
from app.models import User
from app.src.security import LoginForm


flask_security = Blueprint('flask_security', __name__, template_folder='templates')


@flask_security.route('/signin/', methods=['POST'])
def signin():

    form = LoginForm(request.form)

    username = form.username.data
    password = form.password.data

    if not validate_input(username,password):
        flash('Invalid username or password')
        return jsonify(check_error=''), 400

    user = User.query.filter_by(username=username, password=password).first()

    if user is None:
        flash('Invalid username or password')
        return jsonify(check_error='LOGIN_KO'), 401
    if user.role != 'ADMIN':
        login_user(user)
        return jsonify(check_error='LOGIN_KO'), 401

    return jsonify(check_error='OK')


@flask_security.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template('public/index.html', login='LOGIN')


@flask_security.route('/logout/', methods=['GET', 'POST'])
def logout():
    return render_template('security/login.html', check_error='SESSION_EXPIRED')


def validate_input(username, password):
    if (username==None or username=='' or len(username)>20) or (password==None or password==''):
        return False
    else:
        return True
