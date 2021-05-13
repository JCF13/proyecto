from collections import UserDict
from flask_app.app.namespaces.auth.jwt_auth import make_header
from flask.globals import request
from flask_restx import Namespace,Resource
from flask_jwt_extended import create_access_token,create_refresh_token
from flask_restx.marshalling import marshal
import flask_app.app.database.schemas as schema
from flask_app.app.database.dao.userDao import find_user_by_username  
from flask_app.app import bcrypt 

authorization = Namespace('auth')

userSch = schema.userModel
login_req = schema.loginReq
login_res = schema.loginResp
auth_token = schema.auth_token
errorSchema = schema.errorSchema
authorization.add_model('User',userSch)
authorization.add_model('loginRequest',login_req)
authorization.add_model('loginResponse',login_res)
authorization.add_model('auth_token',auth_token)
authorization.add_model('errorSchema',errorSchema)

@authorization.route('/login')
class login(Resource):

    @authorization.expect(login_req)
    @authorization.marshal_with(login_res)
    def post(self):
        load_user = request.get_json()
        user_dict = marshal(load_user,login_req)
        header = make_header(user_dict)
        
        return header
        

        