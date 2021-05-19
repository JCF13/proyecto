from flask_restx import Namespace
from flask_app.app.namespaces.private.schemas import simpleUser

myNS = Namespace('my', 'Interacciones de usuarios entre sí. Follow y Chat.')
myNS.models[simpleUser.name] = simpleUser
