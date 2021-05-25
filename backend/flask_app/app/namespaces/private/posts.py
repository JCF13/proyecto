from backend.flask_app.app.services.commentService import (
    generate_comment, get_post_comments
)
from flask import request, json
from backend.flask_app.app.services.postService import (
    get_all_posts, generate_post, get_comments_by_post, get_post_by_id
)
from backend.flask_app.app.namespaces.private.schemas import (
                    postModel,
                    userModel,
                    commentModel,
                    likeListModel,
                    likeModel,
                    createPostModel,
                    simpleUser,
                    posts,
                    commentUser
                    )
from flask_restx import Namespace, Resource, marshal
from flask_jwt_extended import (
    jwt_required, get_jwt_identity,  verify_jwt_in_request
)

from backend.flask_app.app.database.schemas import PostSchema, PostCommentSchema, UserRegisterSchema

post = Namespace('post', 'todas las rutas de Posts irán a aquí')

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
parser.add_argument('Authorization', location='headers', required=True)

@post.route('/cpost')
class Make_post(Resource):

    @post.expect(createPostModel, parser)
    @jwt_required()
    def post(self):
        newPost = request.get_json()

        marshaledPost = marshal(newPost, createPostModel, skip_none=True)

        generate_post(get_jwt_identity(), marshaledPost)
        # sqlPost = PostSchema()
        # sqlPost.load(marshaledPost,session= db.session)

        return marshaledPost


@post.route('/gposts')
class Get_posts(Resource):

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

        strPosts = sqlPost.dumps(allPosts, many=True)
        h = json.loads(strPosts)
        pos = 0
        for post, j in allPosts, h:
            strComments = sqlPostComment.dumps(get_post_comments(post.post_id), many=True)
            print(strComments)
            j['comments'] = json.loads(strComments)
            #h[i]['comments'] = json.loads(strComments)

        # for post in h:
        #     if len(post['comments']) > 0:
        #         comments = []
        #         for comment in post['comments']:
        #             comments.append(sqlPostComment.dump(comment))
        #         post['comments'] = comments.copy()
            
        return marshal(h,posts)

@post.route('/gpost/<int:id>')
class get_post(Resource):


    # @post.marshal_with(postModel)
    def get(self, id):
        elpost = get_post_by_id(id)
        sqlPost = PostSchema()
        sqlComment = PostCommentSchema()

        strPosts = sqlPost.dumps(elpost)
        jsonPost = json.loads(strPosts)

        strComments = sqlComment.dumps(elpost.comments, many=True)

        jsonPost['comments'] = json.loads(strComments)

        return jsonPost
    
    @post.expect(commentModel, parser)
    @jwt_required()
    def patch(self, id):
        commentJson = request.get_json()
        # marshalledComment = marshal(commentJson, commentModel, skip_none=True)
        generate_comment(get_jwt_identity(), id, commentJson)

        return commentJson
