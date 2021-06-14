import datetime
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import backref
from flask_app.app.database import db
from flask_app.app.database.mixins import CreatedMixin
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column, Integer, String
from flask_security.models import fsqla_v2 as fsqla
from flask_security.models import fsqla as oauth
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

    posts = db.relationship('Post', back_populates='created_by', viewonly=True)
    followers = db.relationship('Followers',primaryjoin='User.id==Followers.followed_id', viewonly=True)
    following = db.relationship('Followers',primaryjoin='User.id==Followers.follower_id', viewonly=True)
    chats = db.relationship('Chat', primaryjoin='User.id==Chat.created_by_fk', viewonly=True)


class Client(db.Model,oauth.FsOauth2ClientMixin):
    __tablename__ = 'oauth2_client'
    # public or confidential
    is_confidential = db.Column(db.Boolean)


class Token(db.Model,oauth.FsTokenMixin):

    pass


class Role(db.Model, fsqla.FsRoleMixin):
    __tablename__ = 'role'

    pass


user_datastore = SQLAlchemySessionUserDatastore(db.session, user_model=User, role_model=Role)


class Followers(db.Model):
    __tablename__ = 'follower'

    follow_id = db.Column(db.Integer, primary_key=True)
    
    followed_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"))
    follower_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"))


class Post(db.Model, CreatedMixin):
    __tablename__ = "post"

    post_id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(20), nullable=True)

    picture = db.Column(db.String, nullable=False)
    
    likes = db.relationship('PostLikes', backref='post')
    comments = db.relationship('PostComment', backref='post')


class PostLikes(db.Model):
    __tablename__ = 'post_likes'

    id = db.Column(db.Integer, primary_key=True)

    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id', ondelete='CASCADE'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))


class PostComment(db.Model, CreatedMixin):
    __tablename__ = 'post_comments'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(20), nullable=False)

    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'))


class Chat(db.Model, CreatedMixin):
    __tablename__ = 'chat'

    chat_id = db.Column(db.Integer, primary_key=True)


    partner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    partner =  db.relationship('User',backref=backref('chat'),foreign_keys=[partner_id])

    messages = db.relationship('ChatMessages', back_populates='chat')


class ChatMessages(db.Model, CreatedMixin):
    __tablename__ = 'chat_messages'

    message_id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(50), nullable=True)
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.chat_id'))

    chat = db.relationship('Chat', back_populates='messages')