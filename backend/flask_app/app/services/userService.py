from flask_app.app.database.schemas import UserRegisterSchema
from flask_app.app.database.models import User
from flask_app.app.database.dao.userDao import generate_user,find_user_by_username
from flask_app.app.database import db
from flask_app.app import bcrypt


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
    creado.profile_pic_fname = user['profile_pic_fname']

    generate_user(creado)
    return True
