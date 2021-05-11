import datetime
import backend.flask_app.app.database.models as models
from backend.flask_app.app.database import ma
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema,SQLAlchemyAutoSchemaOpts
from flask_restx import Model, fields

# class UserSchema(SQLAlchemyAutoSchema):
#     class Meta:
#         model = models.User
#         exclude = ['password']
        
#         include_relationships = True
#         load_instance = True
    
userSchema = Model('userSchema',{
    'user_id' : fields.Integer() ,
    'username' : fields.String(),
    'name' : fields.String(),
    'password' : fields.String(),
    'surname' : fields.String(),
    'email' : fields.String(),
    'profile_pic_path' : fields.String(),
    'profile_pic_fname' : fields.String(),
    # 'posts' : fields.List(fields.Wildcard()),
    # 'chats' : fields.List(fields.Wildcard())
})

auth_token = Model('auth_token',{
    'access_token': fields.String(),
    'refresh_token': fields.String()
})
errorSchema = Model('errorSchema', {
    'error_type': fields.Integer(description='Código identificador del error') ,
    'error_desc': fields.String(description='Descripción del error') ,
})

loginResp =  Model('loginResponse',{
        'date_time': fields.DateTime(default=datetime.datetime.now()),
        'request': fields.String(default='Login'),
        'result': fields.Integer(),
        'your_auth': fields.Nested(auth_token, description='El access_token será tu Header de autorización para siguientes consultas. El refresh_token tarda más en expirar, necesario para generar otro access_token en /mymadisa/refresh '),
        'error': fields.Nested(errorSchema,required=False)
})

loginReq = Model('loginRequest',{
    'username':fields.String(),
    'passwd':fields.String(),
})

class FollowerSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = models.Followers

class PostSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = models.Post
        include_relationships = True
        include_fk = True
        load_instance = True

class PostLikeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = models.PostLikes

class PostCommentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = models.PostComment

class ChatSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = models.Chat
        include_relationships = True
        load_instance = True

class ChatMessageSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = models.ChatMessages
        include_relationships = True

# class NotificationCSchema(SQLAlchemyAutoSchema):
#     class Meta:
#         model = models.NotificationComment
#         include_relationships = True
#         include_fk = True

# class NotificationLSchema(SQLAlchemyAutoSchema):
#     class Meta:
#         model = models.NotificationLike
#         include_relationships = True
#         include_fk = True

# class NotificationFSchema(SQLAlchemyAutoSchema):
#     class Meta:
#         model = models.NotificationFollow
#         include_relationships = True
#         include_fk = True

