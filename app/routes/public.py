from flask import Blueprint, render_template, session,abort
from app.models import Post

public_route = Blueprint('public',__name__, url_prefix='/public')


@public_route.route('/')
def public():
    posts = Post.query.order_by(Post.last_edit.desc()).all()
    return render_template('public/index.html', posts=posts)





