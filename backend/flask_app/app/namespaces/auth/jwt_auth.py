from flask_security.utils import verify_password
from flask_app.app.exceptions import InvalidUsername
from functools import wraps
from flask import request
from flask_restx.marshalling import marshal
from flask_app.app.database.dao.userDao import find_user_by_username, find_user_by_id
from flask_jwt_extended import create_access_token, create_refresh_token


from flask_app.app.namespaces.auth.schemas import auth_token, errorSchema, loginResp


def make_header(user):

    try:
        usuario = find_user_by_username(user['username'])
        verify_password(usuario.password, user['passwd'])
        respuesta = {}
        respuesta['result'] = 0

        tok = {
            "username": user['username'],
            "access_token": create_access_token(identity=usuario.id),
            "refresh_token": create_refresh_token(identity=usuario.id)
            }
        respuesta['your_auth'] = marshal(tok, auth_token, skip_none=True) 

        return marshal(respuesta, loginResp, skip_none=True)
    except InvalidUsername:
        raise InvalidUsername('Credenciales Autorización incorrectas')


def make_header_from_identity(identity):

    usuario = find_user_by_id(identity)
    respuesta = {}
    respuesta['result'] = 0

    tok = {
        "username": usuario.username,
        "access_token": create_access_token(identity=usuario.id),
        "refresh_token": create_refresh_token(identity=usuario.id)
        }
    respuesta['your_auth'] = marshal(tok, auth_token) 

    return marshal(respuesta, loginResp, skip_none=True)
