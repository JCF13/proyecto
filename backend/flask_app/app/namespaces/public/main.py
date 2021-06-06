from flask_app.app.database import db
from flask_restx.resource import Resource
import flask_app.app.database.schemas as schema
import flask_app.app.database.models as model 
from flask_app.app.namespaces import api
from flask_restx import Namespace

main = Namespace('public')
main.model()

postsSch = schema.PostSchema(many=True)

main.model('Post',postsSch)

@main.route('/')
class index(Resource):
    
    def get(self):

        # user = model.User()
        # user.username = 'username'
        # user.name='name'
        # user.surname='surname'
        # user.password='Password'
        pass