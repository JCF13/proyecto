from flask_app.app.database.models import Post
from flask import request, json
from flask_app.app.database import db
from flask_app.app.services.postService import get_all_posts, generate_post
from flask_app.app.namespaces.private.schemas import postModel,userModel,commentModel,likeListModel,likeModel,createPostModel
from flask_restx import Namespace, fields, Resource, marshal


from flask_app.app.database.schemas import PostSchema

post = Namespace('post','todas las rutas de Posts irán a aquí')

post.models[userModel.name] = userModel
post.models[likeModel.name] = likeModel
post.models[likeListModel.name] = likeListModel
post.models[commentModel.name] = commentModel
post.models[postModel.name] = postModel
post.models[createPostModel.name] = createPostModel

@post.route('/cpost')
class make_post(Resource):

    @post.expect(createPostModel)
    def post(self):
        newPost = request.get_json()

        marshaledPost = marshal(newPost,createPostModel,skip_none=True)

        generate_post(marshaledPost)
        # sqlPost = PostSchema()
        # sqlPost.load(marshaledPost,session= db.session)
        
        return marshaledPost

@post.route('/gposts')
class get_posts(Resource):


    def get(self):
        allPosts = get_all_posts()
        sqlPost = PostSchema()
        strPosts = sqlPost.dumps(allPosts,many=True)
        return marshal(json.loads(strPosts),postModel)