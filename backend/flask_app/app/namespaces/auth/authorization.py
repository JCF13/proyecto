from backend.flask_app.app.namespaces.auth.jwt_auth import make_header
from flask.globals import request
from flask_restx import Namespace, Resource
from flask_restx.marshalling import marshal
from backend.flask_app.app.namespaces.auth.schemas import (
    userModel, auth_token, errorSchema,
    loginReq, loginResp, userRegister
)
from backend.flask_app.app.database import db 
from backend.flask_app.app.services.userService import create_user
from backend.flask_app.app.database.schemas import UserRegisterSchema
from backend.flask_app.app.services.logs import complex_file_handler
from backend.flask_app.app.services.logs.refactor_dict import gen_log

authorization = Namespace('auth')
_LEVELLOG_ = 20
 
authorization.logger.addHandler(complex_file_handler)

authorization.models[userModel.name] = userModel
authorization.models[loginReq.name] = loginReq
authorization.models[loginResp.name] = loginResp
authorization.models[auth_token.name] = auth_token
authorization.models[errorSchema.name] = errorSchema
authorization.models[userRegister.name] = userRegister

@authorization.route('/logon')
class Register(Resource):

    def get(self):

        pass

    @authorization.expect(userRegister)
    def post(self):
        to_register = request.get_json()
        marshalled = marshal(to_register, userRegister)
        
        return create_user(marshalled)


class LogOut(Resource):

    def post(self):
        pass


@authorization.route('/login')
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
