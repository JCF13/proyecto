from flask.blueprints import Blueprint
from flask_restx import Api
from flask_app.app.namespaces.auth.authorization import authorization
from flask_app.app.namespaces.private.posts import postNS
from flask_app.app.namespaces.private.user_interaction import myNS
from flask_app.app.namespaces.private.chats import chat
from flask_app.app.namespaces.admin.admin import admin


api_version = '0.01'

managment = Blueprint('routes', __name__)

api = Api(managment, version=api_version, title='Api', description='Descripcion')

api.add_namespace(authorization)
api.add_namespace(postNS)
api.add_namespace(myNS)
api.add_namespace(chat)
api.add_namespace(admin)