import json
from backend.flask_app.app.database.schemas import RoleSchema
from flask_security.utils import verify_password
from backend.flask_app.app.exceptions import InvalidPassword, InvalidUsername
from functools import wraps
from flask import request
from flask_restx.marshalling import marshal
from backend.flask_app.app.database.dao.userDao import find_user_by_username, find_user_by_id
from flask_jwt_extended import create_access_token, create_refresh_token
from backend.flask_app.app.database.models import user_datastore

from backend.flask_app.app.namespaces.auth.schemas import auth_token, errorSchema, loginResp


def make_header(user):
    sqlRole = RoleSchema()

    try:
        usuario = find_user_by_username(user['username'])

        verify_password(user['passwd'], usuario.password)
        if not verify_password(user['passwd'], usuario.password):
            raise InvalidPassword('invalid password')
        respuesta = {}
        respuesta['result'] = 0
        
        strRoles = sqlRole.dumps(usuario.roles, many=True)
        roles = json.loads(strRoles)
        print(roles)
        rol_user = None
        for role in roles:
            if role['name'] == 'Admin':
                rol_user = 'admin'

            elif role['name'] == 'client':
                rol_user = 'client'

        tok = {
            "username": user['username'],
            "access_token": create_access_token(identity=usuario.id),
            "refresh_token": create_refresh_token(identity=usuario.id),
            "role": rol_user
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
