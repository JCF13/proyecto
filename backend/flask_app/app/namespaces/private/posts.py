from datetime import datetime
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
                                                      userModel,
                                                      wildcardResp,
                                                      makePostResp,
                                                      errorSchema
                                                      )
from flask_app.app.services.commentService import (create_comment,
                                                   get_post_comments
                                                   )
from flask_app.app.services.logs import complex_file_handler
from flask_app.app.services.postService import (create_post,
                                                get_by_offset,
                                                get_post_by_id,
                                                delete_post_by_id
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

postNS = Namespace('post', 'todas las rutas de Posts irán a aquí')

postNS.logger.addHandler(complex_file_handler)

postNS.models[userModel.name] = userModel
postNS.models[likeModel.name] = likeModel
postNS.models[likeListModel.name] = likeListModel
postNS.models[commentModel.name] = commentModel
postNS.models[postModel.name] = postModel
postNS.models[createPostModel.name] = createPostModel
postNS.models[simpleUser.name] = simpleUser
postNS.models[posts.name] = posts
postNS.models[commentUser.name] = commentUser
postNS.models[makePostResp.name] = makePostResp
postNS.models[wildcardResp.name] = wildcardResp
postNS.models[errorSchema.name] = errorSchema

parser = postNS.parser()
parser.add_argument('Authorization', location='headers', required=True)


@postNS.route('/cpost')
@postNS.header('Authorization', 'El token se enviará con Bearer antes del mismo')
class Make_post(Resource):

    @postNS.expect(createPostModel, parser)
    @jwt_required()
    def post(self):
        newPost = request.get_json()
        marshaledPost = marshal(newPost, createPostModel, skip_none=True)
        post_created = create_post(get_jwt_identity(), marshaledPost)

        respuesta = {}
        errorRep = {}

        print(post_created)
        respuesta['datetime'] = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
        respuesta['request'] = 'make post'
        if post_created['error_type'] == 'positive':
            respuesta['result'] = 1
            errorRep['error_type'] = None
            errorRep['error_desc'] = None
            elobjresp = {
                'post_id': post_created['post_id'],
                'done': True
            }
            contenido = marshal(elobjresp, makePostResp)
            respuesta['response'] = contenido
            respuesta['error'] = marshal(errorRep, errorSchema)
        print(respuesta)
        elReturn = marshal(respuesta, wildcardResp)
        elLog = gen_log(elReturn, _LEVELLOG_)
        postNS.logger.log(_LEVELLOG_, elLog)
        return elReturn

@postNS.route('/gposts')
class Get_posts(Resource):
    pageParser = postNS.parser()
    parser.add_argument('page', location='args', required=True)

    @postNS.header('Authorization', 'El token se enviará con Bearer antes del mismo', required=True)
    @postNS.expect(parser, pageParser)
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
            post['likes'] = len(post['likes'])
        
        return h

@postNS.route('/gpost/<int:id>')
class get_post(Resource):
    pistIdParser = postNS.parser()
    parser.add_argument('id', location='args', required=True)

    @postNS.expect(parser, pistIdParser)
    @jwt_required()
    def get(self, id):
        elpost = get_post_by_id(request.args.get('id'))
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


@postNS.route('/deletepost/<int:id>')
class DeletePost(Resource):

    @jwt_required()
    def post(self, id):
        return delete_post_by_id(id)
