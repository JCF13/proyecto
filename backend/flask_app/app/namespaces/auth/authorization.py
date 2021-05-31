from flask.globals import request
from flask_restx import Namespace, Resource
from flask_restx.marshalling import marshal
from jwt.exceptions import DecodeError, ExpiredSignatureError
from flask_jwt_extended.exceptions import (
    NoAuthorizationError, InvalidHeaderError, WrongTokenError
)
from flask_app.app.namespaces.auth.jwt_auth import make_header
from flask_app.app.namespaces.auth.schemas import (
    userModel, auth_token, errorSchema,
    loginReq, loginResp, userRegister
)
from flask_app.app.database import db 
from flask_app.app.services.userService import create_user
from flask_app.app.database.schemas import UserRegisterSchema
from flask_app.app.services.logs import complex_file_handler
from flask_app.app.services.logs.refactor_dict import gen_log

authorization = Namespace('auth')
_LEVELLOG_ = 20

authorization.logger.addHandler(complex_file_handler)


authorization.models[userModel.name] = userModel
authorization.models[loginReq.name] = loginReq
authorization.models[loginResp.name] = loginResp
authorization.models[auth_token.name] = auth_token
authorization.models[errorSchema.name] = errorSchema
authorization.models[userRegister.name] = userRegister


@authorization.errorhandler(NoAuthorizationError)
def handler_non_auth(error):
    resultado = { }
    resultado['result'] = -1
    resultado['request'] = ' _ '
    fallo = { }
    fallo['error_type'] = 25
    fallo['error_desc'] = error
    errorDoc = marshal(fallo, errorSchema)
    resultado['error'] = errorDoc

    respuesta = marshal(resultado, loginResp)
    elLog = gen_log(respuesta, _LEVELLOG_)
    authorization.logger.log(_LEVELLOG_, elLog)

    return respuesta


@authorization.errorhandler(AttributeError)
def handler_invalid_username_login(error):

    load_user = request.get_json()
    print(load_user)
    resultado = { }
    resultado['result'] = -1
    resultado['request'] = ' _ '
    auth = { }
    if load_user.get('username'):
        auth['username'] = load_user['username']
        auth['access_token'] = 'inicio de sesion fallido, el usuario o la contraseña están mal'
    authDoc = marshal(auth, auth_token)
    fallo = { }
    fallo['error_type'] = 26
    fallo['error_desc'] = error
    errorDoc = marshal(fallo, errorSchema)
    resultado['your_auth'] = authDoc
    resultado['error'] = errorDoc

    respuesta = marshal(resultado, loginResp)
    elLog = gen_log(respuesta, _LEVELLOG_)
    authorization.logger.log(_LEVELLOG_, elLog)
    return respuesta


@authorization.errorhandler(InvalidHeaderError)
def handler_invalid_header(error):
    resultado = { }
    resultado['result'] = -1
    resultado['request'] = ' _ '
    fallo = { }
    fallo['error_type'] = 26
    fallo['error_desc'] = error
    errorDoc = marshal(fallo, errorSchema)
    resultado['error'] = errorDoc

    respuesta = marshal(resultado, loginResp)
    elLog = gen_log(respuesta, _LEVELLOG_)
    authorization.logger.log(_LEVELLOG_, elLog)
    return respuesta


@authorization.errorhandler(DecodeError)
def handler_decode_token(error):
    resultado = { }
    resultado['result'] = -1
    resultado['request'] = ' _ '
    fallo = { }
    fallo['error_type'] = 27
    fallo['error_desc'] = error
    errorDoc = marshal(fallo, errorSchema)
    resultado['error'] = errorDoc
    respuesta = marshal(resultado, loginResp)

    elLog = gen_log(respuesta, _LEVELLOG_)
    authorization.logger.log(_LEVELLOG_, elLog)

    return respuesta


@authorization.errorhandler(ExpiredSignatureError)
def handler_signature_expired(error):
    resultado = { }
    resultado['result'] = -1
    resultado['request'] = ' _ '
    fallo = { }
    fallo['error_type'] = 28
    fallo['error_desc'] = error
    errorDoc = marshal(fallo, errorSchema)
    resultado['error'] = errorDoc
    respuesta = marshal(resultado, loginResp)

    elLog = gen_log(respuesta, _LEVELLOG_)
    authorization.logger.log(_LEVELLOG_, str(elLog))

    return respuesta


@authorization.errorhandler(WrongTokenError)
def handler_wrong_token(error):
    resultado = { }
    resultado['result'] = -1
    resultado['request'] = ' _ '
    fallo = { }
    fallo['error_type'] = 29
    fallo['error_desc'] = error
    errorDoc = marshal(fallo, errorSchema)
    resultado['error'] = errorDoc
    respuesta = marshal(resultado, loginResp)
    
    elLog = gen_log(respuesta, _LEVELLOG_)
    authorization.logger.log(_LEVELLOG_, elLog)

    return respuesta


@authorization.route('/logon')
class Register(Resource):


    @authorization.expect(userRegister)
    def post(self):
        to_register = request.get_json()
        marshalled = marshal(to_register, userRegister)

        return create_user(marshalled)


class LogOut(Resource):

    def post(self):
        pass


@authorization.route('/login')
@authorization.doc('documentacion de login')
class Login(Resource):

    @authorization.expect(loginReq)
    @authorization.marshal_with(loginResp)
    
    def post(self):

        load_user = request.get_json()
        # request.get_data()

        user_dict = marshal(load_user, loginReq)

        header = make_header(user_dict)
        elLog = gen_log(header, _LEVELLOG_)
        authorization.logger.log(_LEVELLOG_, elLog)

        return header
