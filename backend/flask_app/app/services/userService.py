from flask_app.app.database.schemas import UserRegisterSchema
from flask_app.app.database.models import User, Followers
from flask_app.app.database.dao.userDao import (
    generate_user, find_user_by_username, find_user_by_id, follows_to
)
from flask_app.app.database import db
from flask_app.app import bcrypt


def user_follows_to(follower, followed):
    follows = Followers(followed_id=followed.user_id, follower_id=follower.user_id)
    follows_to(follows)
    pass


def create_user(user):

    if find_user_by_username(user['username']):
        return 'el username ya ha sido registrado'

    creado = User()
    passwordHash = bcrypt.generate_password_hash(user['password'])
    print(user)
    creado.password = passwordHash
    creado.username = user['username']
    creado.name = user['name']
    creado.surname = user['surname']
    creado.email = user['email']
    if user['picture'] is None:
        creado.picture = user['picture']
    else:
        creado.picture = 1
    generate_user(creado)
    return True


def get_user_by_username(username):
    return find_user_by_username(username)


def get_user_by_id(id):
    return find_user_by_id(id)
