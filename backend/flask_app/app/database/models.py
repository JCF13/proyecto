from sqlalchemy.sql.schema import ForeignKey
from backend.flask_app.app.database import db
from backend.flask_app.app.database.mixins import CreatedMixin

class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    
    username = db.Column(db.String(15), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    profile_pic_path = db.Column(db.String(246))
    profile_pic_fname = db.Column(db.String(20))

    posts = db.relationship('Post', back_populates='creator')
    chats = db.relationship('Chat', back_populates='user')
    like_notifications = db.relationship('NotificationLike', back_populates='receiver')
    comment_notifications = db.relationship('NotificationComment', back_populates='receiver')
    follow_notifications = db.relationship('NotificationFollow', back_populates='receiver')


class Followers(db.Model):
    __tablename__ = 'follower'

    follow_id = db.Column(db.Integer, primary_key=True)
    
    followed_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))


class Post(db.Model, CreatedMixin):
    __tablename__ = "post"

    post_id = db.Column(db.Integer, primary_key=True)
    
    caption = db.Column(db.String(20), nullable=False)
    picture_path = db.Column(db.String(246), nullable=False)
    picture_fname = db.Column(db.String(20), nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    creator = db.relationship('User', back_populates='posts')
    likes = db.relationship('PostLikes', back_populates='post')
    comments = db.relationship('PostComment', back_populates='post')


class PostLikes(db.Model):
    __tablename__ = 'post_likes'

    id = db.Column(db.Integer, primary_key=True)

    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    post = db.relationship('Post', back_populates='likes')


class PostComment(db.Model, CreatedMixin):
    __tablename__ = 'post_comments'

    id = db.Column(db.Integer, primary_key=True)
    
    message = db.Column(db.String(20), nullable=False)

    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'))

    post = db.relationship('Post', back_populates='comments')


class Chat(db.Model):
    __tablename__ = 'chat'

    chat_id = db.Column(db.Integer, primary_key=True)

    creator_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    partner_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    user = db.relationship('User', back_populates='chats')
    messages = db.relationship('ChatMessages', back_populates='chat')


class ChatMessages(db.Model, CreatedMixin):
    __tablename__ = 'chat_messages'

    message_id = db.Column(db.Integer, primary_key=True)

    message = db.Column(db.String(50), nullable=False)

    chat_id = db.Column(db.Integer, db.ForeignKey('chat.chat_id'))

    chat = db.relationship('Chat', back_populates='messages')


class NotificationLike(db.Model, CreatedMixin):
    __tablename__ = 'notification_like'

    notification_id = db.Column(db.Integer, primary_key=True)

    

    receiver_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    
    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'))

    receiver = db.relationship('User', back_populates='like_notifications')


class NotificationComment(db.Model, CreatedMixin):
    __tablename__ = 'notification_comment'

    notification_id = db.Column(db.Integer, primary_key=True)

    

    receiver_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    
    comment_id = db.Column(db.Integer, db.ForeignKey('post_comments.id'))

    receiver = db.relationship('User', back_populates='comment_notifications')


class NotificationFollow(db.Model,CreatedMixin):
    __tablename__ = 'notification_follow'

    notification_id = db.Column(db.Integer, primary_key=True)

    
    type = db.Column(db.String(10), nullable=False)

    receiver_id = db.Column(db.Integer, db.ForeignKey('follower.followed_id'))
    

    receiver = db.relationship('User', back_populates='follow_notifications')