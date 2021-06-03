
from datetime import datetime
from flask_app.app.exceptions import EmailUsed, UsernameUsed

from sqlalchemy.exc import IntegrityError
from flask_app.app.database.schemas import UserRegisterSchema
from flask_app.app.database.models import User, Followers
from flask_app.app.database.dao.userDao import (
    generate_user, find_user_by_username, find_user_by_id, follows_to,
    find_user_by_email, set_profile_pic
)
from flask_app.app import bcrypt
from flask_app.app.database import db
from flask_app.app.services.imageService import save_picture


def user_follows_to(follower, followed):
    follows = Followers(followed_id=followed.user_id,
                        follower_id=follower.user_id)
    follows_to(follows)
    pass


def verify_user(user):
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
    return True


def create_user(user):
    creado = User()
    try:
        passwordHash = bcrypt.generate_password_hash(user['password'])
        print(user)
        creado.password = passwordHash
        creado.username = user['username']
        creado.name = user['name']
        creado.surname = user['surname']
        # creado.email = None
        creado.email = user['email']

        if user['picture'] != '':
            creado.picture = user['picture']
        else:
            creado.picture = 1
        generate_user(creado)
        return {
            'type': 'positive',
            'message': 'Usuario registrado correctamente'
        }
    except (EmailUsed, UsernameUsed) as expt:
        print('_____________')
        print(expt.args)
        print('_____________')

        if expt.statement == 'username':
            raise UsernameUsed(params=user['username'], orig=IntegrityError, statement='El email no es valido')
            
        elif expt.statement == 'email':
            raise EmailUsed(params=user['email'], orig=IntegrityError, statement='El email no es valido')


def get_user_by_username(username):
    return find_user_by_username(username)


def get_user_by_id(id):
    return find_user_by_id(id)


def update_profile_pic(user):
    user_to_update = get_user_by_id(user['user'])
    user_to_update.picture = save_picture(user['picture'], str(user['user'])+str(datetime.now()).replace(' ', '-').replace('.', '').replace(':', ''))
    set_profile_pic(user_to_update)
    return {
        'type': 'positive',
        'message': 'Foto de perfil actualizada correctamente'
    }