from sqlalchemy import Column, Integer, String, Text, DateTime
from app import db
from datetime import *


class Post(db.Model):
    __tablename__ = 'post'
    id = Column(db.Integer, primary_key=True)
    title = Column(String(255), unique=True)
    body = Column(Text)
    created_at = Column(DateTime, index=True, default=datetime.utcnow)
    last_edit = Column(DateTime, index=True, onupdate=datetime.utcnow, default=datetime.utcnow)
    author_id = Column(Integer, db.ForeignKey('users.id'))
