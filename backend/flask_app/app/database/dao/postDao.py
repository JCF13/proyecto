from backend.flask_app.app.database.models import Post, PostLikes
from backend.flask_app.app.database import db


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


def add_like(like: PostLikes):
    db.session.add(like)
    db.session.commit()


def delete_post(post: Post):
    db.session.delete(post)
    db.session.commit()


def find_like_by_user_and_post(user_id, post_id):
    return PostLikes.query.filter(PostLikes.post_id==post_id, PostLikes.user_id==user_id).first()


def delete_like(like: PostLikes):
    db.session.delete(like)
    db.session.commit()