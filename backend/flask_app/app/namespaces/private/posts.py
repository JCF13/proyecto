from flask_app.app.services.commentService import generate_comment
from flask_app.app.database.models import Post
from flask import request, json
from flask_app.app.database import db
from flask_app.app.services.postService import get_all_posts, generate_post, get_post_by_id
from flask_app.app.namespaces.private.schemas import postModel,userModel,commentModel,likeListModel,likeModel,createPostModel, simpleUser, posts, commentUser
from flask_restx import Namespace, fields, Resource, marshal
from flask_jwt_extended import jwt_required, get_jwt_identity

from flask_app.app.database.schemas import PostSchema, PostCommentSchema

post = Namespace('post','todas las rutas de Posts irán a aquí')

post.models[userModel.name] = userModel
post.models[likeModel.name] = likeModel
post.models[likeListModel.name] = likeListModel
post.models[commentModel.name] = commentModel
post.models[postModel.name] = postModel
post.models[createPostModel.name] = createPostModel
post.models[simpleUser.name] = simpleUser
post.models[posts.name] = posts
post.models[commentUser.name] = commentUser

parser = post.parser()
parser.add_argument('Authorization', location='headers',required=True)

@post.route('/cpost')
class make_post(Resource):

    @post.expect(createPostModel,parser)
    @jwt_required()
    def post(self):
        newPost = request.get_json()

        marshaledPost = marshal(newPost,createPostModel,skip_none=True)

        generate_post(get_jwt_identity(),marshaledPost)
        # sqlPost = PostSchema()
        # sqlPost.load(marshaledPost,session= db.session)
        
        return marshaledPost

@post.route('/gposts')
class get_posts(Resource):


    def get(self):
        allPosts = get_all_posts()
        sqlPost = PostSchema()
        sqlPostComment = PostCommentSchema()
        # for post in allPosts:
        #     if len(post.comments) > 0:
        #         comentarios = []
        #         for comment in post.comments:
        #             comentarios.append(sqlPostComment.load(comment))
        #         post.comments = comentarios

            # for key,val in post.__dict__.items():
            #     print(key,'  _   ',val)
            # print('çambio')

        strPosts = sqlPost.dumps(allPosts,many=True)
        h = json.loads(strPosts)
        # for post in h:
        #     if len(post['comments']) > 0:
        #         comments = []
        #         for comment in post['comments']:
        #             comments.append(sqlPostComment.dump(comment))
        #         post['comments'] = comments.copy()
            
        return marshal(h,posts)

@post.route('/gpost/<int:id>')
class get_post(Resource):
    
    def get(self,id):
        elpost = get_post_by_id(id)
        sqlPost = PostSchema()
        strPosts = sqlPost.dumps(elpost)
        return marshal(json.loads(strPosts),postModel)
    
    @post.expect(commentModel,parser)
    @jwt_required()
    def post(self,id):
        commentJson = request.get_json()
        marshalledComment = marshal(commentJson,commentModel,skip_none=True)
        generate_comment(get_jwt_identity(),id,marshalledComment)

        return marshalledComment