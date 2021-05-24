from flask_app.app.database.schemas import UserRegisterSchema
from flask_app.app.database.models import User, Followers
from flask_app.app.database.dao.userDao import (
    generate_user,find_user_by_username, find_user_by_id, follows_to
)
from flask_app.app import bcrypt
from flask_app.app.database import db

def user_follows_to(follower, followed):
    follows = Followers(followed_id=followed.user_id, follower_id=follower.user_id)
    follows_to(follows)
    pass

def create_user(user):
    if user['username'] != '' \
        and user['password'] != '' \
        and user['email'] != '' \
        and user['name'] != '':
        if find_user_by_username(user['username']):
            return {
                'type': 'error',
                'message': 'El nombre de usuario ya está en uso'
        }

        if find_user_by_email(user['email']):
            return {
                'type': 'error',
                'message': 'El correo electrónico ya está en uso'
            }

        creado = User()
        passwordHash = bcrypt.generate_password_hash(user['password'])
        print(user)
        creado.password = passwordHash
        creado.username = user['username']
        creado.name = user['name']
        creado.surname = user['surname']
        creado.email = user['email']
        creado.profile_pic_fname = user['profile_pic_fname']

        generate_user(creado)
        return True
    else:
        return {
            'type': 'error',
            'message': 'Los datos no son correctos'
        }
def get_user_by_username(username):
    return find_user_by_username(username)
def get_user_by_id(id):
    return find_user_by_id(id)