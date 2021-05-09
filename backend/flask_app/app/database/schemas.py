import backend.flask_app.app.database.models as models
from backend.flask_app.app.database import ma
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema,SQLAlchemyAutoSchemaOpts


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = models.User
        exclude = ['password']
        only = ['user_id','username','name','surname','email']
        include_relationships = True
        load_instance = True
    posts = ma.List(ma.HyperlinkRelated('posts_detail'))
    chats = ma.List(ma.HyperlinkRelated('chats_detail'))


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

class NotificationCSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = models.NotificationComment
        include_relationships = True
        include_fk = True

class NotificationLSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = models.NotificationLike
        include_relationships = True
        include_fk = True

class NotificationFSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = models.NotificationFollow
        include_relationships = True
        include_fk = True

