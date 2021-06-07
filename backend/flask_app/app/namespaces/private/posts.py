from backend.flask_app.app.database.schemas import (PostCommentSchema, PostLikeSchema,
                                                    PostSchema,
                                                    UserRegisterSchema)
from backend.flask_app.app.namespaces.private.schemas import (commentModel,
                                                              commentUser,
                                                              createPostModel,
                                                              likeListModel,
                                                              likeModel,
                                                              postModel, posts,
                                                              simpleUser,
                                                              userModel)
from backend.flask_app.app.services.commentService import (generate_comment,
                                                           get_post_comments)
from backend.flask_app.app.services.logs import complex_file_handler
from backend.flask_app.app.services.postService import (generate_post,
                                                        get_by_offset,
                                                        get_post_by_id,
                                                        delete_post_by_id)
from flask import current_app, json, request
from flask_jwt_extended import (get_jwt_identity, jwt_required,
                                verify_jwt_in_request
                                )
from flask_restx import Namespace, Resource, marshal
from backend.flask_app.app.services.userService import get_user_by_id
from backend.flask_app.app.namespaces.auth.schemas import userProfile, creator
from backend.flask_app.app.services.imageService import get_picture

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


@post.route('/cpost')
class Make_post(Resource):

    @post.expect(createPostModel, parser)
    @jwt_required()
    def post(self):
        newPost = request.get_json()

        marshaledPost = marshal(newPost, createPostModel, skip_none=True)

        return generate_post(get_jwt_identity(), marshaledPost)


@post.route('/gposts/<int:page>')
class Get_posts(Resource):

    @jwt_required()
    def get(self, page):
        user = get_user_by_id(get_jwt_identity())

        following = []

        for follow in user.following:
            following.append(get_user_by_id(follow.followed_id))

        allPosts = get_by_offset(page, following)

        sqlPost = PostSchema()
        sqlLike = PostLikeSchema()

        jsonPosts = []
        for post in allPosts:
            strLikes = sqlLike.dumps(post.likes, many=True)
            jsonLikes = json.loads(strLikes)
            
            for like in jsonLikes:
                like['user'] = marshal(get_user_by_id(like['user_id']), creator, skip_none=True)

            strPost = sqlPost.dumps(post)
            jsonPost = json.loads(strPost)
            jsonPost['likes'] = jsonLikes

            for like in jsonPost['likes']:
                jsonPost['liked'] = False
                if user.id == like['user_id']:
                    jsonPost['liked'] = True
            
            user = get_user_by_id(jsonPost['created_by_fk'])
            user_resp = marshal(user, creator, skip_none=True)
            jsonPost['creator'] = user_resp
            jsonPosts.append(jsonPost)

        return jsonPosts


@post.route('/gpost/<int:id>')
class get_post(Resource):

    @jwt_required()
    def get(self, id):
        myself = get_user_by_id(get_jwt_identity())

        elpost = get_post_by_id(id)
        sqlPost = PostSchema()
        sqlComment = PostCommentSchema()

        strPosts = sqlPost.dumps(elpost)
        jsonPost = json.loads(strPosts)

        strComments = sqlComment.dumps(elpost.comments, many=True)
        jsonComments = json.loads(strComments)

        for comment in jsonComments:
            comment['user'] = marshal(get_user_by_id(comment['created_by']), creator, skip_none=True)
        
        jsonPost['comments'] = jsonComments

        user = get_user_by_id(jsonPost['created_by_fk'])
        creator_post = marshal(user, creator, skip_none=True)
        jsonPost['creator'] = creator_post

        return jsonPost


@post.route('/deletepost/<int:id>')
class DeletePost(Resource):

    @jwt_required()
    def post(self, id):
        return delete_post_by_id(id)
