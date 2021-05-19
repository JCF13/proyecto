from flask_app.app.namespaces.auth.jwt_auth import make_header
from flask.globals import request
from flask_restx import Namespace, Resource
from flask_restx.marshalling import marshal
from flask_app.app.namespaces.auth.schemas import (
    userModel, auth_token, errorSchema,
    loginReq, loginResp, userRegister
)
from flask_app.app.database import db 
from flask_app.app.services.userService import create_user
from flask_app.app.database.schemas import UserRegisterSchema

authorization = Namespace('auth')

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
        create_user(marshalled)
        
        print('done')
        
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

        return header
