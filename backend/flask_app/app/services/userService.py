
from datetime import datetime
from flask_mail import Message
import os

from flask_security.utils import hash_password, verify_password
from backend.flask_app.app.exceptions import EmailUsed, RequiredEmail, RequiredName, RequiredPassword, RequiredUsername, UsernameUsed
from flask_security.registerable import generate_confirmation_link
from sqlalchemy.exc import IntegrityError
from backend.flask_app.app.exceptions import InvalidPassword
from backend.flask_app.app.database.schemas import UserRegisterSchema
from backend.flask_app.app.database.models import User, Followers, user_datastore
from backend.flask_app.app.database.dao.userDao import (
    delete, find_users_by, generate_user, find_user_by_username, find_user_by_id, follows_to,
    find_user_by_email, get_follow, set_password, set_profile_pic, set_username, unfollows_to, find_all
)
from backend.flask_app.app.database import db
from backend.flask_app.app import mail
from backend.flask_app.app.services.imageService import save_picture


def user_follows_to(follower, followed):
    if follower.id != followed.id:
        follows = Followers(followed_id=followed.id, follower_id=follower.id)
        follows_to(follows)
        return {
            'error_type': 'positive',
            'error_desc': 'Has seguido a ' + followed.username
        }
    else:
        return {
            'error_type': 'error',
            'error_desc': 'No puedes seguirte a tí mismo'
        }


def user_unfollows_to(follower, unfollowed):
    unfollow = get_follow(follower.id, unfollowed.id)
    unfollows_to(unfollow)
    return {
        'error_type': 'positive',
        'error_desc': 'Has dejado de seguir a ' + unfollowed.username
    }


def verify_user(user):
    if find_user_by_username(user['username']):
        return {
            'error_type': 'error',
            'error_desc': 'El nombre de usuario ya está en uso'
        }

    if find_user_by_email(user['email']):
        return {
            'error_type': 'error',
            'error_desc': 'El correo electrónico ya está en uso'
        }
    return True


def send_confirm_mail(user):
    lik, token = generate_confirmation_link(user)
    msg = Message(subject='Confirm your account '+user.username,
                 recipients=[user.email],
                 body="""
                 Here you got your Confirmation Link, click above for Confirm
                 """+lik,
                )
    with mail.connect() as mailConn:
        mailConn.send(msg)


def create_user(user):
    if user['username'] == '':
        raise RequiredUsername(params='Username: None', orig=IntegrityError, statement='El username es requerido para el registro, Condinción')
        
    elif user['name'] == '':
        raise RequiredName(params='Name: None', orig=IntegrityError, statement='El nombre es requerido para el registro, Condinción')

    elif user['password'] == '':
        raise RequiredPassword(params='Password: None', orig=IntegrityError, statement='La password es requerida para el registro, Condinción')
        
    elif user['email'] == '':
        raise RequiredEmail(params='Email: None', orig=IntegrityError, statement='El email es requerido para el registro, Condinción')
    creado = User()
    try:
        passwordHash = hash_password(user['password'])
        creado.password = passwordHash
        creado.username = user['username']
        creado.name = user['name']
        creado.surname = user['surname']
        creado.email = user['email']
        creado.picture = user['picture']
        if not user_datastore.find_role('client'):
            client_role = user_datastore.create_role(name='client')
        user_datastore.add_role_to_user(user=creado, role='client')
        user_datastore.activate_user(creado)
        user_datastore.set_uniquifier(creado)
        generate_user(creado)
        send_confirm_mail(creado)
        user_datastore.commit()
        return {
            'error_type': 'positive',
            'error_desc': 'Usuario registrado correctamente'
        }
    except (EmailUsed, UsernameUsed, RequiredUsername,
            RequiredName, RequiredPassword, RequiredEmail) as expt:
        if expt.params == 'UNIQUE':
            if expt.statement == 'username':
                raise UsernameUsed(params=user['username'], orig=IntegrityError, statement='El username no es valido')
                
            elif expt.statement == 'email':
                raise EmailUsed(params=user['email'], orig=IntegrityError, statement='El email no es valido')
        elif expt.params == 'NOT NULL':

            if expt.statement == 'username':
                raise RequiredUsername(params='Username: None', orig=IntegrityError, statement='El username es requerido para el registro')
                
            elif expt.statement == 'name':
                raise RequiredName(params='Name: None', orig=IntegrityError, statement='El nombre es requerido para el registro')

            elif expt.statement == 'password':
                raise RequiredPassword(params='Password: None', orig=IntegrityError, statement='La password es requerida para el registro')
                
            elif expt.statement == 'email':
                raise RequiredEmail(params='Email: None', orig=IntegrityError, statement='El email es requerido para el registro')


def get_user_by_username(username):
    return find_user_by_username(username)


def get_user_by_id(id):
    return find_user_by_id(id)


def update_profile_pic(user):
    user_to_update = get_user_by_id(user['user'])
    user_to_update.picture = save_picture(user['picture'], str(user['user'])+str(datetime.now()).replace(' ', '-').replace('.', '').replace(':', ''))
    set_profile_pic(user_to_update)
    
    return {
        'error_type': 'positive',
        'error_desc': 'Foto de perfil actualizada correctamente'
    }


def search_users(search, user_id):
    return find_users_by(search, user_id)


def update_username(user, username):
    user.username = username
    set_username(user)

    return {
        'error_type': 'positive',
        'error_desc': 'Nombre de usuario cambiado correctamente'
    }


def update_password(user, password, new_password):
    if not verify_password(password, user.password):
        raise InvalidPassword('invalid password')
    else:
        user.password = hash_password(new_password)
        set_password(user)
        return {
            'error_type': 'positive',
            'error_desc': 'Contraseña actualizada correctamente'
        }


def get_all_users():
    return find_all()


def delete_user(id):
    user = find_user_by_id(id)
    posts = user.posts

    delete(user)
    
    for post in posts:
        os.remove(post.picture)
    
    return {
        'error_type': 'positive',
        'error_desc': 'Usuario eliminado'
    }