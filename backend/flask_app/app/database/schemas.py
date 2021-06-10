from sqlalchemy.orm import load_only
import backend.flask_app.app.database.models as models
from backend.flask_app.app.database import ma
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class UserRegisterSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = models.User
        load_instance = True
        
        
# class UserSchema(SQLAlchemyAutoSchema):
#     class Meta:
#         model = models.User
#         exclude = ['password']
        
#         include_relationships = True
#         load_instance = True
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
        include_relationships = True
        include_fk = True

class PostCommentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = models.PostComment
        include_relationships = True

class ChatSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = models.Chat
        include_relationships = True
        load_instance = True

class ChatMessageSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = models.ChatMessages
        include_relationships = True

class RoleSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = models.Role