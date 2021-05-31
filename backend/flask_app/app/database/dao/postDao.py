from flask_app.app.database.models import Post
from flask_app.app.database import db


def generate_post(post: Post):
    """
    Takes a Post object and save it at the data base

    :param post: the actual object which will be
                 saved at the data base
    """
    db.session.add(post)
    db.session.commit()


def find_by_offset(page):
    """
    Return all the Post objects of the data base
    """
    return Post.query.limit(10).offset(page*10)


def find_all_posts():
    """
    Return all the Post objects of the data base
    """
    return Post.query.all()


def find_post_by_id(id):
    """
    Return the Post object wich is identical
    with the param of the data base
    :param id: int
    """
    return Post.query.filter(Post.post_id == id).first()