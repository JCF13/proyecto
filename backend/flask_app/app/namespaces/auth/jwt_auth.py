import datetime
import jwt
import base64
import os
from functools import wraps
from flask import make_response, json,request, Response
from flask_restx.marshalling import marshal
from flask_app.app.database.dao.userDao import find_user_by_username
from flask_jwt_extended import create_access_token, create_refresh_token

from flask_app.app import bcrypt,JSONEncoder
from flask_app.app.database.schemas import auth_token, errorSchema, loginResp




def make_header(user):
    valido = False
    print('make')
    print(user)
    usuario = find_user_by_username(user['username'])
    print(usuario)
    if bcrypt.check_password_hash(usuario.password,user['passwd']):
        valido = True 
            
    if valido == True:
        respuesta = {}
        respuesta['result'] = 0
        
        tok = {
            "access_token": create_access_token(identity=user),
            "refresh_token": create_refresh_token(identity=user)
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
