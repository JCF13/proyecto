from flask.globals import request
from flask_restx import Namespace,Resource
from flask_jwt_extended import create_access_token,create_refresh_token
from flask_restx.marshalling import marshal
import backend.flask_app.app.database.schemas as schema
from backend.flask_app.app.database.dao.userDao import find_user_by_username  
from backend.flask_app.app import bcrypt 

authorization = Namespace('auth')

userSch = schema.UserSchema(many=False)
login_req = schema.loginReq
login_res = schema.loginResp
authorization.add_model('User',userSch)
authorization.add_model('loginRequest',login_req)
authorization.add_model('loginResponse',login_res)

@authorization.route('/login')
class login(Resource):

    @authorization.expect(login_req)
    @authorization.marshal_with(login_res)
    def post(self):
        load_user = request.get_json()
        user_dict = marshal(load_user,login_req)
        print(user_dict.get('username'))
        user = find_user_by_username(user_dict.get('username'))
        hashed_pass = bcrypt.check_password_hash(user.password,user_dict.get('password'))

        if user and bcrypt.check_password_hash(user.password,user_dict.get('password')):
            print(user)
            adicional = marshal(user,schema.UserSchema)
            tmp = {
                'access_token':create_access_token(user.username,additional_claims=adicional),
                'refresh_token':create_refresh_token(user.username,additional_claims=adicional)
            }
            return marshal(tmp,schema.loginResp)
        

        