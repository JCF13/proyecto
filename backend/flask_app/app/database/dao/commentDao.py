from flask_app.app.database.models import PostComment
from flask_app.app.database import db

def create_commentPost(comment: PostComment):
    db.session.add(comment)
    db.session.commit()
    

def find_all_posts():
    return PostComment.query.all()

def find_post_by_id(id):
    return PostComment.query.filter(PostComment.post_id == id).first()