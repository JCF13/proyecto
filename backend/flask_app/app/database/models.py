import datetime
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import backref
from flask_app.app.database import db
from flask_app.app.database.mixins import CreatedMixin
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column, Integer, String
from flask_security.models import fsqla_v2 as fsqla
from flask_security.datastore import SQLAlchemySessionUserDatastore



class User(db.Model, fsqla.FsUserMixin):
    __tablename__ = 'user'
    
    # user_id = Column('user_id', Integer, primary_key=True)
    # username = db.Column(db.String(15), nullable=False, unique = True)
    name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(20), nullable=True)
    # password = db.Column(db.String(20), nullable=False)
    # email = db.Column(db.String(50), nullable=False, unique = True)
    picture = db.Column(db.String, nullable=True)
    #picture = db.Column(db.Integer, db.ForeignKey('profile_image.image_id'))

    posts = db.relationship('Post', back_populates='created_by', viewonly=True)
    followers = db.relationship('Followers',primaryjoin='User.id==Followers.follower_id', viewonly=True)
    following = db.relationship('Followers',primaryjoin='User.id==Followers.followed_id', viewonly=True)
    chats = db.relationship('Chat', primaryjoin='User.id==Chat.created_by_fk', viewonly=True)
    # like_notifications = db.relationship('NotificationLike', back_populates='receiver')
    # comment_notifications = db.relationship('NotificationComment', back_populates='receiver')
    # follow_notifications = db.relationship('NotificationFollow', back_populates='receiver')


class Role(db.Model, fsqla.FsRoleMixin):
    __tablename__ = 'role'

    pass


user_datastore = SQLAlchemySessionUserDatastore(db.session, user_model=User, role_model=Role)


class Followers(db.Model):
    __tablename__ = 'follower'

    follow_id = db.Column(db.Integer, primary_key=True)
    
    followed_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Post(db.Model, CreatedMixin):
    __tablename__ = "post"

    post_id = db.Column(db.Integer, primary_key=True)
    #nullables cambiados
    caption = db.Column(db.String(20), nullable=True)

    #picture = db.Column(db.Integer, db.ForeignKey('post_image.image_id'))
    picture = db.Column(db.String, nullable=False)
    
    likes = db.relationship('PostLikes', backref='post')
    comments = db.relationship('PostComment', backref='post')


class PostLikes(db.Model):
    __tablename__ = 'post_likes'

    id = db.Column(db.Integer, primary_key=True)

    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # post = db.relationship('Post', back_populates='likes')


class PostComment(db.Model, CreatedMixin):
    __tablename__ = 'post_comments'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(20), nullable=False)

    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'))

    # post = db.relationship('Post', back_populates='comments')


class Chat(db.Model, CreatedMixin):
    __tablename__ = 'chat'

    chat_id = db.Column(db.Integer, primary_key=True)


    partner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    partner =  db.relationship('User',backref=backref('chat'),foreign_keys=[partner_id])

    messages = db.relationship('ChatMessages', back_populates='chat')


class ChatMessages(db.Model, CreatedMixin):
    __tablename__ = 'chat_messages'

    message_id = db.Column(db.Integer, primary_key=True)
# nullable cambiado a mmessage
    message = db.Column(db.String(50), nullable=True)
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.chat_id'))
    #image  = db.Column(db.Integer, db.ForeignKey('chat_image.chat_id'), nullable=True)

    chat = db.relationship('Chat', back_populates='messages')


#class Image(CreatedMixin):

#    @declared_attr
#    def image_id(self):
#        return Column(Integer, primary_key=True)

#    @declared_attr
#    def image(self):
#        return Column(String(), nullable=False)


#class ChatImage(db.Model, Image):
#    __tablename__ = 'chat_image'

#    chat_id = db.Column(db.Integer, db.ForeignKey('chat.chat_id'))

#class PostImage(db.Model, Image):
#    __tablename__ = 'post_image'

#    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'))

#class ProfileImage(db.Model):
#    __tablename__ = 'profile_image'
#    image_id = db.Column(Integer, primary_key=True)
#    image = db.Column(String(), nullable=False)
#    created_on = db.Column(db.DateTime, default=datetime.datetime.now(), nullable=False)
    

# class NotificationLike(db.Model, CreatedMixin):
#     __tablename__ = 'notification_like'

#     notification_id = db.Column(db.Integer, primary_key=True)
#     post_id = db.Column(db.Integer, db.ForeignKey('post_likes.id'))

#     receiver_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
#     receiver = db.relationship('User', back_populates='like_notifications', foreign_keys=[receiver_id,CreatedMixin.created_by_fk])


# class NotificationComment(db.Model, CreatedMixin):
#     __tablename__ = 'notification_comment'

#     notification_id = db.Column(db.Integer, primary_key=True)

#     receiver_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
#     receiver =  db.relationship('User',backref=backref('notification_comment'),foreign_keys=[receiver_id])
    
#     comment_id = db.Column(db.Integer, db.ForeignKey('post_comments.id'))



# class NotificationFollow(db.Model,CreatedMixin):
#     __tablename__ = 'notification_follow'

#     notification_id = db.Column(db.Integer, primary_key=True)

    
#     type = db.Column(db.String(10), nullable=False)

#     receiver_id = db.Column(db.Integer, db.ForeignKey('follower.followed_id'))
#     receiver = db.relationship('User', back_populates='follow_notifications')