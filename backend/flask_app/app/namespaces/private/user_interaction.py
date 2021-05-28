from flask import request, json
from flask.helpers import send_file
from flask_restx import Namespace, Resource, marshal
from backend.flask_app.app.namespaces.private.schemas import (
    simpleUser, followModel, profilePicture, picture
)
from backend.flask_app.app.namespaces.auth.schemas import userProfile, picture
from flask_jwt_extended import (
    jwt_required, get_jwt_identity,  verify_jwt_in_request
)
from backend.flask_app.app.services.userService import get_user_by_id, get_user_by_username, user_follows_to
#from backend.flask_app.app.services.imageService import create_image
from backend.flask_app.app.services.logs import complex_file_handler
from backend.flask_app.app.database.schemas import PostSchema
from backend.flask_app.app.services.imageService import get_picture

myNS = Namespace('my', 'Interacciones de usuarios entre sí. Follow y Chat.')

myNS.logger.addHandler(complex_file_handler)
print(myNS.logger.handlers)

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
        user_followed = get_user_by_username(body['user']['username'])
        foll = user_follows_to(user_follower, user_followed)
        print(foll)
        print(user_followed)
        print(user_follower)
        pass


@myNS.route('/getUser/<string:username>')
class GetUser(Resource):
    def get(self, username):
        user = get_user_by_username(username)
        sqlPost = PostSchema()

        strPosts = sqlPost.dumps(user.posts, many=True)

        resp = marshal(user, userProfile, skip_none=True)
        resp['posts'] = json.loads(strPosts)
        
        return resp 


@myNS.route('/image')
class SendImage(Resource):

    def post(self):
        image = request.get_json()
        pic = get_picture(image)
        return marshal(pic, picture, skip_none=True)