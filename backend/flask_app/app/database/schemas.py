import backend.flask_app.app.database.models as models
from backend.flask_app.app.database import ma


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.User
        exclude = ['password']
        include_relationships = True
        load_instance = True

class FollowerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.Followers

class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.Post
        include_relationships = True
        load_instance = True

class PostLikeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.PostLikes

class PostCommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.PostComment

class ChatSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.Chat
        include_relationships = True
        load_instance = True

class ChatMessageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.ChatMessages
        include_relationships = True

class NotificationCSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.NotificationComment

class NotificationLSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.NotificationLike

class NotificationFSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.NotificationFollow

