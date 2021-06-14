from flask_app.app.database.models import PostComment
from flask_app.app.database import db


def generate_commentPost(comment: PostComment):
    """
    Takes a PostComment object and save it at the data base

    :param comment: the actual object which will be
                    saved at the data base
    """
    db.session.add(comment)
    db.session.flush()
    db.session.commit()
    return comment.message


def find_all_posts():
    """
    Return all the PostComment objects of the data base
    """
    return PostComment.query.all()


def find_comments_by_post_id(id):
    """
    Takes a int and find a post wich post_id is like the param

    :param id: int
    """
    return PostComment.query.filter(PostComment.post_id == id).all()