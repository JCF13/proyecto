from flask.blueprints import Blueprint
from flask_restx import Api

api_version = '0.01'

managment = Blueprint('routes',__name__)

api = Api(managment,version=api_version,title='Api',description='Descripcion')
