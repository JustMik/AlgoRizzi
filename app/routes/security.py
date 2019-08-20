from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import current_user, login_user
from app.models import User
from app.src.security import LoginForm
from wtforms.validators import ValidationError



flask_security = Blueprint('flask_security', __name__, template_folder='templates')

@flask_security.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    # GET case
    if request.method=='GET':
        if current_user.is_authenticated:
            return redirect(url_for('admin.index'))
        return render_template('security/login.html', form=form, check_error='')

    elif request.method=='POST':
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username, password=password).first()

        if user is None:
            flash('Invalid username or password')
            return render_template('security/login.html', form=form, check_error='LOGIN_KO')

        login_user(user)
        return redirect(url_for('admin.index'))



@flask_security.route('/logout/', methods=['GET', 'POST'])
def logout():
    return render_template('security/login.html', check_error='SESSION_EXPIRED')


def validate_input(username, password):
    if (username==None or username=='' or len(username)>20) or (password==None or password==''):
        return False
    else:
        return True
