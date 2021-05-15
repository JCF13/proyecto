from collections import UserDict
from flask_app.app.namespaces.auth.jwt_auth import make_header
from flask.globals import request
from flask_restx import Namespace,Resource
from flask_jwt_extended import create_access_token,create_refresh_token
from flask_restx.marshalling import marshal
from flask_app.app.database.schemas import userModel,auth_token,errorSchema,loginReq,loginResp
from flask_app.app.database.dao.userDao import find_user_by_username  
from flask_app.app.cli.generate import bcrypt 

authorization = Namespace('auth')

authorization.models[userModel.name] = userModel
authorization.models[loginReq.name] = loginReq
authorization.models[loginResp.name] = loginResp
authorization.models[auth_token.name] = auth_token
authorization.models[errorSchema.name] = errorSchema

@authorization.route('/login')
class login(Resource):

    @authorization.expect(loginReq)
    @authorization.marshal_with(loginResp)
    def post(self):
        load_user = request.get_json()
        print(load_user)
        user_dict = marshal(load_user,loginReq)
        print(user_dict)
        header = make_header(load_user)
        
        return header
        

        