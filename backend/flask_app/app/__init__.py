import datetime
import decimal

from flask_security.confirmable import generate_confirmation_link

from flask import Flask, json
from flask_cors import CORS
from flask_migrate import Migrate, MigrateCommand
from flask_jwt_extended import JWTManager
from flask_security.utils import hash_password
from flask_app.app.config import Config
from flask_app.app.database import db, ma
from flask_security import Security
from flask_app.app.database.models import user_datastore
from flask_security.mail_util import MailUtil
from flask_mail import Mail, Message
cors = CORS()
jwt = JWTManager()
migrate = Migrate(db=db)
security = Security()
mail = Mail()

class JSONEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        elif isinstance(obj, datetime.date):
            return obj.strftime('%d/%m/%Y')
        return super(JSONEncoder, self).default(obj)


def create_app():
    app = Flask(__name__.split('.')[1])
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app)

    app.json_encoder = JSONEncoder
    jwt.init_app(app)
    cors.init_app(app)
    mail.init_app(app)
    security.init_app(app, user_datastore)

    from flask_app.app.namespaces import managment
    import flask_app.app.cli as cli 
    app.register_blueprint(managment)
    app.register_blueprint(cli.gen)

    @app.before_first_request
    def create_first_user():
        if not user_datastore.find_user(email="tjimenezsblanca@gmail.com"):
            firstuser = user_datastore.create_user(email="tjimenezsblanca@gmail.com", username='ToniJSB', name='ToniJSB', password=hash_password("ToniJSB"))
            adminrole = user_datastore.create_role(name='Admin', permissions='can_create_users')
            user_datastore.add_role_to_user(firstuser, adminrole)

    return app


app = create_app()
