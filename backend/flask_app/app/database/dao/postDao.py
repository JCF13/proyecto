from flask_app.app.database.models import Post
from flask_app.app.database import db


def generate_post(post: Post):
    """
    Takes a Post object and save it at the data base

    :param post: the actual object which will be
                 saved at the data base
    """
    db.session.add(post)
    db.session.flush()
    db.session.commit()
    return post.post_id


def find_by_offset(page, users):
    """
    Return all the Post objects of the data base
    """
    ids = []
    for user in users:
        ids.append(user.id)
    print(ids)

    return Post.query.filter(Post.created_by_fk.in_(ids)).order_by(Post.created_on).limit(10).offset(page*10)
    #return Post.query.limit(10).offset(page*10)


def find_post_by_id(id):
    """
    Return the Post object wich is identical
    with the param of the data base
    :param id: int
    """
    return Post.query.filter(Post.post_id == id).first()


def find_by_offset_and_followed(page):
    pass