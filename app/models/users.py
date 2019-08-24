from sqlalchemy import Column, Integer, String
from app.database import Base
from flask_login import UserMixin
from app import login, db

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(120), unique=True)
    role = Column(String(20))
    post = db.relationship('Post', backref='author', lazy='dynamic')

    def __init__(self, username=None, password=None, role=None):
        self.username = username
        self.password = password
        self.role = role

    def __repr__(self):
        return  self.username


    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))


    def get_user(self):
        return {'id': self.id, 'username':self.username, 'password':self.password, 'role':self.role}