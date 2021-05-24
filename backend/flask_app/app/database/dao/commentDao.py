from backend.flask_app.app.database.models import PostComment
from backend.flask_app.app.database import db


def create_commentPost(comment: PostComment):
    db.session.add(comment)
    db.session.commit()


def find_all_posts():
    return PostComment.query.all()


def find_comments_by_post_id(id):
    for key in PostComment.query.filter(PostComment.post_id == id):
        print(key.message)
        print('_____________')
    return PostComment.query.filter(PostComment.post_id == id).all()