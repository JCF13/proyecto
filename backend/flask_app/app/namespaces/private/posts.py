from flask_app.app.database.schemas import (PostCommentSchema,
                                            PostSchema,
                                            UserRegisterSchema
                                            )
from flask_app.app.namespaces.private.schemas import (commentModel,
                                                      commentUser,
                                                      createPostModel,
                                                      likeListModel,
                                                      likeModel,
                                                      postModel, posts,
                                                      simpleUser,
                                                      userModel
                                                      )
from flask_app.app.services.commentService import (create_comment,
                                                   get_post_comments
                                                   )
from flask_app.app.services.logs import complex_file_handler
from flask_app.app.services.postService import (create_post,
                                                get_by_offset,
                                                get_post_by_id
                                                )
from flask import current_app, json, request
from flask_jwt_extended import (get_jwt_identity, jwt_required,
                                verify_jwt_in_request
                                )
from flask_restx import Namespace, Resource, marshal
from flask_app.app import _LEVELLOG_
from flask_app.app.services.userService import get_user_by_id
from flask_app.app.namespaces.auth.schemas import userProfile, creator
from flask_app.app.services.imageService import get_picture
from flask_app.app.services.logs.refactor_dict import gen_log

post = Namespace('post', 'todas las rutas de Posts irán a aquí')

post.logger.addHandler(complex_file_handler)

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


@post.route('/cpost', doc = {'post':'documentacion post'} )
class Make_post(Resource):

    @post.expect(createPostModel, parser)
    @jwt_required()
    def post(self):
        newPost = request.get_json()

        marshaledPost = marshal(newPost, createPostModel, skip_none=True)
        post_created = create_post(get_jwt_identity(), marshaledPost)
        postSchema = PostSchema()
        postJson = json.loads(postSchema.dumps(post_created))
        print(postJson)
        elLog = gen_log(postJson, _LEVELLOG_)
        post.logger.log(_LEVELLOG_, elLog)
        return 

@post.route('/gposts')
class Get_posts(Resource):
    pageParser = post.parser()
    parser.add_argument('page', location='args', required=True)

    @post.expect(parser, pageParser)
    @jwt_required()
    def get(self):
        page = request.args.get('page')
        user = get_user_by_id(get_jwt_identity())

        following = []

        for follow in user.following:
            following.append(get_user_by_id(follow.followed_id))

        allPosts = get_by_offset(page, following)

        sqlPost = PostSchema()

        strPosts = sqlPost.dumps(allPosts, many=True)
        h = json.loads(strPosts)
        for post in h:
            user = get_user_by_id(post['created_by_fk'])
            user_resp = marshal(user, creator, skip_none=True)
            post['creator'] = user_resp

        return h

@post.route('/gpost/<int:id>')
class get_post(Resource):
    pistIdParser = post.parser()
    parser.add_argument('id', location='args', required=True)

    # @post.marshal_with(postModel)

    @post.expect(parser, pistIdParser)
    def get(self, id):
        elpost = get_post_by_id(request.args.get('id'))
        sqlPost = PostSchema()
        sqlComment = PostCommentSchema()

        strPosts = sqlPost.dumps(elpost)
        jsonPost = json.loads(strPosts)

        strComments = sqlComment.dumps(elpost.comments, many=True)

        jsonPost['comments'] = json.loads(strComments)

        user = get_user_by_id(jsonPost['created_by_fk'])
        creator_post = marshal(user, creator, skip_none=True)
        jsonPost['creator'] = creator_post

        print(jsonPost)

        return jsonPost


    @post.expect(commentModel, parser)
    @jwt_required()
    def patch(self, id):
        commentJson = request.get_json()
        # marshalledComment = marshal(commentJson, commentModel, skip_none=True)
        
        create_comment(get_jwt_identity(), id, commentJson)

        return commentJson
