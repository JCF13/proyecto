from flask_app.app.database.models import Post
from flask_app.app.database import db

def create_post(post: Post):
    db.session.add(post)
    db.session.commit()
    

def find_all_posts():
    return Post.query.all()