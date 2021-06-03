from backend.flask_app.app.database.models import User, Followers
from backend.flask_app.app.database import db


def find_user_by_username(username: str):
    """
    Return the user object wich is identical
    with the param of the data base

    :param id: int
    """
    return User.query.filter(User.username == username).first()


def find_user_by_id(id: int):
    """
    Return the user object wich is identical
    with the param of the data base

    :param id: int
    """
    return User.query.filter(User.user_id == id).first()


def find_user_by_email(email: str):
    return User.query.filter(User.email == email).first()


def generate_user(user: User):
    """
    Takes a User object and save it at the data base

    :param user: the actual object which will be
                 saved at the data base
    """
    db.session.add(user)
    db.session.commit()


def follows_to(follow: Followers):
    """
    Takes a Followers object and save it at the data base

    :param follow: the actual object which will be
                 saved at the data base
    """
    db.session.add(follow)
    db.session.commit()


def unfollows_to(follow: Followers):
    db.session.delete(follow)
    db.session.commit()


def get_follow(follower: int, followed: int):
    return Followers.query.filter(Followers.follower_id==follower, Followers.followed_id==followed).first()


def set_profile_pic(user: User):
    db.session.add(user)
    db.session.commit()
    return 


def find_users_by(search: str, user_id: int):
    return User.query.filter(User.username.like('%'+search+'%'), User.user_id!=user_id).limit(10)


def set_username(user: User):
    db.session.add(user)
    db.session.commit()


def set_password(user: User):
    db.session.add(user)
    db.session.commit()