from backend.flask_app.app.database import db
from flask_restx.resource import Resource

from backend.flask_app.app.namespaces import api
from flask_restx import Namespace

main = Namespace('public')



@main.route('/')
class index(Resource):
    
    def get(self):

        # user = model.User()
        # user.username = 'username'
        # user.name='name'
        # user.surname='surname'
        # user.password='Password'
        pass