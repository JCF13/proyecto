from backend.flask_app.app.database.schemas import FollowerSchema, PostSchema
from backend.flask_app.app.namespaces.auth.schemas import (creator, picture,
                                                           userProfile)
from backend.flask_app.app.namespaces.private.schemas import (followModel,
                                                              picture,
                                                              profilePicModel,
                                                              profilePicture,
                                                              simpleUser)
from backend.flask_app.app.services.commentService import generate_comment
from backend.flask_app.app.services.imageService import get_picture
#from backend.flask_app.app.services.imageService import create_image
from backend.flask_app.app.services.logs import complex_file_handler
from backend.flask_app.app.services.postService import dislike, new_like
from backend.flask_app.app.services.userService import (get_user_by_id,
                                                        get_user_by_username,
                                                        search_users, update_password,
                                                        update_profile_pic,
                                                        update_username,
                                                        user_follows_to,
                                                        user_unfollows_to)
from flask import json, request
from flask.helpers import send_file
from flask_jwt_extended import (get_jwt_identity, jwt_required,
                                verify_jwt_in_request)
from flask_restx import Namespace, Resource, marshal

myNS = Namespace('my', 'Interacciones de usuarios entre sí. Follow y Chat.')

myNS.logger.addHandler(complex_file_handler)

myNS.models[simpleUser.name] = simpleUser
myNS.models[followModel.name] = followModel
myNS.models[profilePicture.name] = profilePicture
myNS.models[picture.name] = picture

parser = myNS.parser()
parser.add_argument('Authorization', location='headers', required=True)


@myNS.route('/foll')
class Follow(Resource):

    @myNS.expect(followModel, parser)
    @jwt_required()
    def patch(self):
        username_follower = get_jwt_identity()
        body = request.get_json()
        user_follower = get_user_by_id(username_follower)
        user_followed = get_user_by_id(body['user'])
        foll = user_follows_to(user_follower, user_followed)
        
        return foll


@myNS.route('/unfoll')
class  Unfollow(Resource):

    @myNS.expect(followModel, parser)
    @jwt_required()
    def patch(self):
        username_follower = get_jwt_identity()
        body = request.get_json()
        user_follower = get_user_by_id(username_follower)
        user_unfollowed = get_user_by_id(body['user'])
        unfoll = user_unfollows_to(user_follower, user_unfollowed)

        return unfoll


@myNS.route('/searchUsers')
class SearchUsers(Resource):
    @jwt_required()
    def post(self):
        search_by = request.get_json()
        user = get_user_by_id(get_jwt_identity())

        users = search_users(search_by['search'], user.id)
        users_json = []

        for user in users:
            users_json.append(marshal(user, creator, skip_none=True))

        return users_json


@myNS.route('/getFollowers')
class GetFollowers(Resource):

    @jwt_required()
    def get(self):
        myself = get_user_by_id(get_jwt_identity())
        followers = []

        for user in myself.followers:
            followers.append(marshal(get_user_by_id(user.follower_id), creator, skip_none=True))

        return followers


@myNS.route('/getFollowing')
class GetFollowing(Resource):

    @jwt_required()
    def get(self):
        myself = get_user_by_id(get_jwt_identity())
        following = []

        for user in myself.following:
            following.append(marshal(get_user_by_id(user.followed_id), creator, skip_none=True))

        return following


@myNS.route('/getUser/<string:username>')
class GetUser(Resource):
    @jwt_required()
    def get(self, username):
        user = get_user_by_id(get_jwt_identity())
        user_profile = get_user_by_username(username)
        following = False
        follow_you = False

        sqlPost = PostSchema()

        for foll in user_profile.followers:
            if get_user_by_id(foll.follower_id).username == user.username:
                following = True

        for foll in user.followers:
            if get_user_by_id(foll.follower_id).username == username:
                follow_you = True

        strPosts = sqlPost.dumps(user_profile.posts, many=True)

        resp = marshal(user_profile, creator, skip_none=True)
        resp['posts'] = json.loads(strPosts)
        resp['followers'] = len(user_profile.followers)
        resp['following'] = len(user_profile.following)
        resp['followed'] = following
        resp['followYou'] = follow_you
        
        return resp


@myNS.route('/getProfile')
class GetProfile(Resource):
    @jwt_required()
    def get(self):
        user = get_user_by_id(get_jwt_identity())
        sqlPost = PostSchema()

        strPosts = sqlPost.dumps(user.posts, many=True)

        resp = marshal(user, creator, skip_none=True)
        resp['posts'] = json.loads(strPosts)
        resp['followers'] = len(user.followers)
        resp['following'] = len(user.following)

        return resp


@myNS.route('/image')
class SendImage(Resource):

    def post(self):
        image = request.get_json()
        pic = get_picture(image)
        return marshal(pic, profilePicModel, skip_none=True)


@myNS.route('/profilepic')
class SetProfilePic(Resource):

    @jwt_required()
    def post(self):
        pic_req = request.get_json()
        pic_req['user'] = get_jwt_identity()
        profile_pic = marshal(pic_req, profilePicModel, skip_none=True)
        return update_profile_pic(pic_req)


@myNS.route('/comment')
class NewComment(Resource):

    @jwt_required()
    def patch(self):
        commentJson = request.get_json()
        user_id = get_jwt_identity()

        return generate_comment(user_id, commentJson['post_id'], commentJson['message'])


@myNS.route('/like')
class NewLike(Resource):

    @jwt_required()
    def patch(self):
        likeJson = request.get_json()
        user_id = get_jwt_identity()

        return new_like(user_id, likeJson['post_id'])


@myNS.route('/dislike')
class DisLike(Resource):

    @jwt_required()
    def post(self):
        dislikeJson = request.get_json()
        user_id = get_jwt_identity()

        return dislike(user_id, dislikeJson['post_id'])


@myNS.route('/changeUsername')
class ChangeUsername(Resource):

    @jwt_required()
    def post(self):
        new_username = request.get_json()
        user = get_user_by_id(get_jwt_identity())

        return update_username(user, new_username['username'])


@myNS.route('/changePassword')
class ChangePassword(Resource):

    @jwt_required()
    def post(self):
        new_password = request.get_json()
        user = get_user_by_id(get_jwt_identity())

        return update_password(user, new_password['password'], new_password['new_password'])