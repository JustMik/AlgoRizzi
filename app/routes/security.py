from flask import Blueprint, render_template, session,abort

security_route = Blueprint('sec',__name__)

@security_route.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template('public/login.html')
