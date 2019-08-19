from flask import Blueprint, render_template, session,abort

flask_security = Blueprint('flask_security', __name__, template_folder='templates')

@flask_security.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template('security/login.html')
