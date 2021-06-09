from flask.globals import request
from flask_restx import Namespace, Resource, marshal
from backend.flask_app.app.services.logs import complex_file_handler
from flask_jwt_extended import get_jwt_identity, jwt_required
from backend.flask_app.app.services.userService import delete_user, get_all_users
from backend.flask_app.app.namespaces.auth.schemas import creator

admin = Namespace('admin', 'Rutas para administrador')

admin.logger.addHandler(complex_file_handler)

parser = admin.parser()
parser.add_argument('Authorization', location='headers', required=True)


@admin.route('/getAll')
class GetAllUsers(Resource):

    @jwt_required()
    def get(self):
        users = get_all_users()
        usersJson = []

        for user in users:
            usersJson.append(marshal(user, creator, skip_none=True))

        return usersJson


@admin.route('/delete')
class DeleteUser(Resource):
    
    @jwt_required()
    def post(self):
        user = request.get_json()

        return delete_user(user['user_id'])