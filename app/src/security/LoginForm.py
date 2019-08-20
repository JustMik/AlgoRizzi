from wtforms import StringField, Form, validators, PasswordField, BooleanField


class LoginForm(Form):
    username = StringField('username', validators=[validators.DataRequired()])
    password = PasswordField('password', validators=[validators.DataRequired()])

