import datetime
from flask_restx import Model, fields
from backend.flask_app.app.namespaces.private.schemas import postModel, posts

userModel = Model('User',{     
    'user_id': fields.Integer(),
    'username': fields.String(),
    'name': fields.String(),
    'password': fields.String(),
    'surname': fields.String(),
    'email': fields.String(),
    'picture': fields.String(),
})

userRegister = Model('userRegister', {
    'username': fields.String(),
    'name': fields.String(),
    'surname': fields.String(),
    'password': fields.String(),
    'email': fields.String(),
    'picture': fields.String(),
})

auth_token = Model('auth_token', {
    'username': fields.String(),
    'access_token': fields.String(),
    'refresh_token': fields.String()

})

errorSchema = Model('error', {
    'error_type': fields.Integer(description='Código identificador del error'),
    'error_desc': fields.String(description='Descripción del error'),
})

loginResp = Model('loginResponse', {
        'date_time': fields.DateTime(default=datetime.datetime.now()),
        'request': fields.String(default='Login'),
        'result': fields.Integer(),
        'your_auth': fields.Nested(auth_token, description='''
        El access_token será tu Header de autorización
        para siguientes consultas. El refresh_token tarda más en expirar,
        '''),
        'error': fields.Nested(errorSchema, required=False)
})

loginReq = Model('loginRequest',{
    'username': fields.String(),
    'passwd': fields.String(),
})

userProfile = Model('userProfile', {
    'id': fields.Integer(),
    'username': fields.String(),
    'profile_pic': fields.String(),
    'posts': fields.Nested(postModel)
})

creator = Model('creator', {
    'id': fields.Integer(),
    #'user_id': fields.Integer(),
    'username': fields.String(),
    'picture': fields.String(),
})

picture = Model('picture', {
    'picture': fields.String()
})
