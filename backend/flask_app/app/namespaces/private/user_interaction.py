from flask import request
from flask_restx import Namespace, Resource
from flask_app.app.namespaces.private.schemas import (
    simpleUser, followModel
)
from flask_jwt_extended import (
    jwt_required, get_jwt_identity,  verify_jwt_in_request
)
from flask_app.app.services.userService import get_user_by_id, get_user_by_username, user_follows_to


myNS = Namespace('my', 'Interacciones de usuarios entre sí. Follow y Chat.')
myNS.models[simpleUser.name] = simpleUser
myNS.models[followModel.name] = followModel

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