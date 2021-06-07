from datetime import datetime
from flask_restx import Model, fields

userModel = Model('User', {
    'user_id': fields.Integer(),
    'username': fields.String(),
    'name': fields.String(),
    'password': fields.String(),
    'email': fields.String(),
    'picture': fields.String(),
    # 'posts' : fields.List(fields.Wildcard()),
    # 'chats' : fields.List(fields.Wildcard())
})

simpleUser = Model('simpleUser', {
    'id': fields.Integer(),
    'username': fields.String(),
    'profilePic': fields.String()
})

userProfile = Model('UserProfile', {
    'username': fields.String(),
    'name': fields.String(),
    'picture': fields.String(),
    # 'posts' : fields.List(fields.Wildcard()),
    # 'chats' : fields.List(fields.Wildcard())
})

picture = Model('picture', {
    'kind': fields.String(description='CHOICES: profile, chat, post'),
    'blurb': fields.String(),
    'post_id': fields.Integer()
})

profilePicture = Model('profilePicture',{
    'blurb': fields.String()
})

likeModel = Model('Like', {
    'user': fields.Nested(simpleUser),
    'like': fields.Boolean(default=False)
})

likeListModel = Model('LikeList', {
    'cantidad': fields.Integer(),
    'lista': fields.List(fields.Integer())
})

commentModel = Model('Comment', {
    # 'created_by_fk': fields.Integer(),
    'message': fields.String(max=150),
    # 'date_time': fields.String(),
})

createPostModel = Model('PostCreate', {
    'caption': fields.String(),
    'picture': fields.String()
    #'path': fields.String(),
    #'fname': fields.String(),
})

postModel = Model('Post',{
    # 'id': fields.Integer(attribute='post_id'),
    'user_id': fields.Integer(attribute='created_by_fk'),
    'caption': fields.String(attribute='caption'),
    'path': fields.String(attribute='picture_path'),
    'fname': fields.String(attribute='picture_fname'),
    'likes': fields.Nested(likeListModel),
    'comments': fields.List(fields.Nested(commentModel)),
})

commentUser = Model('commentUser', {
    # 'id': fields.Integer(),
    'user': fields.Nested(simpleUser, attribute='created_by'),
    'message': fields.String(),
    'creationDate': fields.DateTime(default=datetime.now(), attribute='created_on')
})

listComments = Model('commentList', {
    'list': fields.List(fields.Nested(commentUser))
})

posts = Model('allPosts', {
    'id': fields.Integer(attribute='post_id'),
    'picture': fields.String(attribute='picture'),
    'caption': fields.String(attribute='caption'),
    'creationDate': fields.DateTime(default=datetime.now(), attribute='created_on'),
    'creator': fields.List(fields.Nested(simpleUser, attribute='created_by')),
    'comments': fields.List(fields.Nested(commentUser, attribute='comments', as_list=True))
})

followModel = Model('followModel', {
    'user': fields.Integer(),
})

profilePicModel = Model('profilePicModel', {
    'user': fields.Integer(),
    'picture': fields.String()
})

errorSchema = Model('error', {
    'error_type': fields.Integer(description='Código identificador del error'),
    'error_desc': fields.String(description='Descripción del error'),
})


wildcardResp = Model('response', {
        'date_time': fields.DateTime(default=datetime.now()),
        'request': fields.String(),
        'result': fields.Integer(),
        'response': fields.Nested([postModel, followModel], description='''
        El access_token será tu Header de autorización
        para siguientes consultas. El refresh_token tarda más en expirar,
        '''),
        'error': fields.Nested(errorSchema, required=False)
})

createChat = Model('createChat', {
    'user': fields.Integer(),
    'partner': fields.Integer()
})

chatModel = Model('chatModel', {
    'chat_id': fields.Integer(),
    'user': fields.Nested(simpleUser, attribute='created_by_fk'),
    'partner': fields.Nested(simpleUser),
})