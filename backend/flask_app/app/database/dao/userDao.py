from sqlalchemy.exc import IntegrityError
from flask_app.app.exceptions import InvalidUsername
from flask_app.app.database.models import User, Followers
from flask_app.app.database import db


def find_user_by_username(username: str):
    """
    Return the user object wich is identical
    with the param of the data base

    :param id: int
    """
    try:
        user = User.query.filter(User.username == username).first()
        print(user.username)
        print('user')
        return user
    except AttributeError:
        raise InvalidUsername('invalid username')


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
    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        print(IntegrityError('fallo de username'))

def follows_to(follow: Followers):
    """
    Takes a Followers object and save it at the data base

    :param follow: the actual object which will be
                 saved at the data base
    """
    db.session.add(follow)
    db.session.commit()


def set_profile_pic(user: User):
    db.session.add(user)
    db.session.commit()
    return 
