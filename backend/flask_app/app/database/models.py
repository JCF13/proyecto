from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import backref
from flask_app.app.database import db
from flask_app.app.database.mixins import CreatedMixin

class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    profile_pic_path = db.Column(db.String(246), nullable= True)
    profile_pic_fname = db.Column(db.String(20), nullable= True)

    posts = db.relationship('Post', back_populates='created_by', viewonly=True)
    followers = db.relationship('Followers',primaryjoin='User.user_id==Followers.followed_id', viewonly=True)
    following = db.relationship('Followers',primaryjoin='User.user_id==Followers.follower_id', viewonly=True)
    chats = db.relationship('Chat', primaryjoin='User.user_id==Chat.created_by_fk', viewonly=True)
    # like_notifications = db.relationship('NotificationLike', back_populates='receiver')
    # comment_notifications = db.relationship('NotificationComment', back_populates='receiver')
    # follow_notifications = db.relationship('NotificationFollow', back_populates='receiver')




class Followers(db.Model):
    __tablename__ = 'follower'

    follow_id = db.Column(db.Integer, primary_key=True)
    
    followed_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))


class Post(db.Model, CreatedMixin):
    __tablename__ = "post"

    post_id = db.Column(db.Integer, primary_key=True)
    #nullables cambiados
    caption = db.Column(db.String(20), nullable=True)
    picture_path = db.Column(db.String(246), nullable=True)
    picture_fname = db.Column(db.String(20), nullable=True)
    
    likes = db.relationship('PostLikes', backref='post')
    comments = db.relationship('PostComment', backref='post')


class PostLikes(db.Model):
    __tablename__ = 'post_likes'

    id = db.Column(db.Integer, primary_key=True)

    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

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


    partner_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    partner =  db.relationship('User',backref=backref('chat'),foreign_keys=[partner_id])

    messages = db.relationship('ChatMessages', back_populates='chat')


class ChatMessages(db.Model, CreatedMixin):
    __tablename__ = 'chat_messages'

    message_id = db.Column(db.Integer, primary_key=True)
# nullable cambiado a mmessage
    message = db.Column(db.String(50), nullable=False)

    chat_id = db.Column(db.Integer, db.ForeignKey('chat.chat_id'))

    chat = db.relationship('Chat', back_populates='messages')


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