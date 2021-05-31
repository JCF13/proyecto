from functools import wraps
from flask import request
from flask_restx.marshalling import marshal
from flask_app.app.services.userService import get_user_by_username
from flask_jwt_extended import create_access_token, create_refresh_token

from flask_app.app import bcrypt
from flask_app.app.namespaces.auth.schemas import auth_token, errorSchema, loginResp


def make_header(user):
    """
        Takes a dict with required params for
        generate an access_JWT and a refresh_JWT

        :param user: dict(username,passwd)
    """

    valido = False
    print(user['username'])
    usuario = get_user_by_username(user['username'])
    print(usuario)
    if bcrypt.check_password_hash(usuario.password, user['passwd']):
        valido = True

    if valido is True:
        respuesta = {}
        respuesta['result'] = 0

        tok = {
            "username": usuario.username,
            "access_token": create_access_token(identity=usuario.user_id),
            "refresh_token": create_refresh_token(identity=usuario.user_id)
            }
        respuesta['your_auth'] = marshal(tok,auth_token,skip_none=True) 

        return marshal(respuesta,loginResp,skip_none=True)
    else:
        respuesta = {}
        fallo = {
            'error_type': 24 ,
            'error_desc':  'Credenciales Autorización incorrectas' ,
        }
        respuesta['result'] = -1
        
        respuesta['error'] = marshal(fallo,errorSchema,skip_none=True) 
    
        return marshal(respuesta,loginResp,skip_none=True)
