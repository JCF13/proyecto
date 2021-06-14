from datetime import datetime
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from flask import abort
from flask.globals import current_app, request, session
from flask_restx import Namespace, Resource
from flask_restx.marshalling import marshal
from jwt.exceptions import DecodeError, ExpiredSignatureError
from flask_jwt_extended import jwt_required
from flask_jwt_extended.utils import get_jwt_identity, get_jwt_request_location
from flask_jwt_extended.view_decorators import verify_jwt_in_request
from flask_jwt_extended.exceptions import (
    NoAuthorizationError, InvalidHeaderError, WrongTokenError
)
from flask_app.app import db
from flask_app.app import _LEVELLOG_, oauth2
from flask_app.app.exceptions import EmailUsed, InvalidUsername, InvalidPassword
from flask_app.app.namespaces.auth.jwt_auth import make_header, make_header_from_identity

from flask_app.app.namespaces.auth.schemas import (
    userModel, auth_token, errorSchema,
    loginReq, loginResp, userRegister
)
from flask_app.app.services.userService import create_user, get_user_by_id

from flask_app.app.services.logs import complex_file_handler
from flask_app.app.services.logs.refactor_dict import gen_log
from flask_app.app.services.oauthService import (
    create_token, get_tokens, get_token_by_accs_tok, get_token_by_ref_tok,
    generate_token, get_client_by_id
    )




authorization = Namespace('auth')
 
authorization.logger.addHandler(complex_file_handler)

authorization.models[userModel.name] = userModel
authorization.models[loginReq.name] = loginReq
authorization.models[loginResp.name] = loginResp
authorization.models[auth_token.name] = auth_token
authorization.models[errorSchema.name] = errorSchema
authorization.models[userRegister.name] = userRegister


@authorization.errorhandler(NoAuthorizationError)
def handler_non_auth(error):
    resultado = {}
    resultado['result'] = -1
    resultado['request'] = ' _ '
    fallo = {}
    fallo['error_type'] = 25
    fallo['error_desc'] = error
    errorDoc = marshal(fallo, errorSchema)
    resultado['error'] = errorDoc

    respuesta = marshal(resultado, loginResp)

    elLog = gen_log(respuesta, _LEVELLOG_)
    authorization.logger.log(_LEVELLOG_, elLog)

    return respuesta


@authorization.errorhandler(InvalidUsername)
def handler_invalid_username_login(error):

    load_user = request.get_json()
    resultado = {}
    resultado['result'] = -1
    resultado['request'] = ' _ '

    fallo = {}
    fallo['error_type'] = 26
    fallo['error_desc'] = error
    errorDoc = marshal(fallo, errorSchema)
    resultado['error'] = errorDoc

    respuesta = marshal(resultado, loginResp)

    elLog = gen_log(respuesta, _LEVELLOG_)
    authorization.logger.log(_LEVELLOG_, elLog)
    return respuesta


@authorization.errorhandler(InvalidPassword)
def handler_invalid_password(error):

    load_user = request.get_json()
    resultado = {}
    resultado['result'] = -1
    resultado['request'] = 'login / register'

    fallo = {}
    fallo['error_type'] = 26
    fallo['error_desc'] = error
    errorDoc = marshal(fallo, errorSchema)
    resultado['error'] = errorDoc
    
    respuesta = marshal(resultado, loginResp)

    elLog = gen_log(respuesta, _LEVELLOG_)
    authorization.logger.log(_LEVELLOG_, elLog)
    return respuesta


@authorization.errorhandler(SQLAlchemyError)
def handler_email_used_login(error):

    load_user = request.get_json()
    resultado = {}
    resultado['result'] = -1
    resultado['request'] = ' _ '

    fallo = {}
    fallo['error_type'] = 26
    fallo['error_desc'] = error.statement
    errorDoc = marshal(fallo, errorSchema)
    resultado['error'] = errorDoc
    
    respuesta = marshal(resultado, loginResp)

    elLog = gen_log(respuesta, _LEVELLOG_)
    authorization.logger.log(_LEVELLOG_, elLog)
    return respuesta


@authorization.errorhandler(InvalidHeaderError)
def handler_invalid_header(error):
    resultado = {}
    resultado['result'] = -1
    resultado['request'] = ' _ '
    fallo = {}
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
    resultado = {}
    resultado['result'] = -1
    resultado['request'] = ' _ '
    fallo = {}
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
    resultado = {}
    resultado['result'] = -1
    resultado['request'] = ' _ '
    fallo = {}
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
    resultado = {}
    resultado['result'] = -1
    resultado['request'] = ' _ '
    fallo = {}
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
        marshalled = marshal(to_register, userRegister, skip_none=True)

        elLog = gen_log(marshalled, _LEVELLOG_)
        authorization.logger.log(_LEVELLOG_, elLog)
        return create_user(marshalled)




parser = authorization.parser()
parser.add_argument('Authorization', location='headers', required=True)


@authorization.route('/login')
class Login(Resource):

    @authorization.expect(loginReq)
    @authorization.marshal_with(loginResp)
    def post(self):

        load_user = request.get_json()

        user_dict = marshal(load_user, loginReq)

        header = make_header(user_dict)
        elLog = gen_log(header, _LEVELLOG_)
        authorization.logger.log(_LEVELLOG_, elLog)

        return header


    @authorization.expect(parser)
    @jwt_required(refresh=True)
    def get(self):
        verify_jwt_in_request(refresh=True)
        user_identity = get_jwt_identity()
        header = make_header_from_identity(user_identity)
        header['request'] = request.environ['PATH_INFO']
        authorization.logger.log(_LEVELLOG_, gen_log(header, _LEVELLOG_))
        return header




@oauth2.clientgetter
def load_client(client_id):
    return get_client_by_id(client_id)


@oauth2.tokengetter
def load_token(access_token=None, refresh_token=None):
    if access_token:
        return get_token_by_accs_tok(access_token)
    elif refresh_token:
        return get_token_by_ref_tok(refresh_token)


@oauth2.tokensetter
def save_token(token, request, *args, **kwargs):
    toks = get_tokens(request)
    # make sure that every client has only one token connected to a user
    for t in toks:
        db.session.delete(t)

    expires_in = token.get('expires_in')
    expires = datetime.datetime.utcnow() + datetime.timedelta(seconds=expires_in)

    tok = create_token(token, expires, request)
    return tok


@authorization.route('/login/google')
class LoginOauth(Resource):
    
    @authorization.expect(parser)
    def post(self):
        print(session.get('oauth'))
        
        print('______________')
        print(request.cookies.__dict__)
        print('______________')
        print(request.args)
        print('______________')
        print(request.oauth)
        print('______________')
        
        pass