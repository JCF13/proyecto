from flask import request
from backend.flask_app.app.database import db
from backend.flask_app.app.services.postService import get_all_posts
from backend.flask_app.app.namespaces.private.schemas import postModel,userModel,commentModel,likeListModel,likeModel
from flask_restx import Namespace, fields, Resource, marshal


from backend.flask_app.app.database.schemas import PostSchema

post = Namespace('post','todas las rutas de Posts irán a aquí')

post.models[userModel.name] = userModel
post.models[likeModel.name] = likeModel
post.models[likeListModel.name] = likeListModel
post.models[commentModel.name] = commentModel
post.models[postModel.name] = postModel

@post.route('/cpost')
class make_post(Resource):

    @post.expect(postModel)
    def post(self):
        newPost = request.get_json()
        marshaledPost = marshal(newPost,postModel)
        sqlPost = PostSchema()
        sqlPost.load(marshaledPost,session= db.session)
        print(sqlPost.__dict__)
        return marshal(newPost,postModel)