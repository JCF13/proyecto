from flask_restx import Model, fields

userModel = Model('User',{
    'user_id' : fields.Integer() ,
    'username' : fields.String(),
    'name' : fields.String(),
    'password' : fields.String(),
    'email' : fields.String(),
    'profile_pic_path' : fields.String(),
    'profile_pic_fname' : fields.String(),
    # 'posts' : fields.List(fields.Wildcard()),
    # 'chats' : fields.List(fields.Wildcard())
})

likeModel = Model('Like',{
    'user': fields.Nested(userModel),
    'like': fields.Boolean(default=False)
})

likeListModel = Model('LikeList',{
    'cantidad': fields.Integer(),
    'lista': fields.List(fields.Integer())
})

commentModel = Model('Comment',{
    'created_by': fields.Integer(),
    'message': fields.String(max=150),

})

createPostModel = Model('PostCreate',{
'user_id': fields.Integer(),
'caption': fields.String(),
'path': fields.String(),
'fname': fields.String(),
})

postModel = Model('Post',{
'id': fields.Integer(attribute='post_id'),
'user_id': fields.Integer(attribute='created_by_fk'),
'caption': fields.String(attribute='caption'),
'path': fields.String(attribute='picture_path'),
'fname': fields.String(attribute='picture_fname'),
'likes': fields.Nested(likeListModel,allow_null=True ),
'comments': fields.List(fields.Nested(commentModel,allow_null=True)),
})



