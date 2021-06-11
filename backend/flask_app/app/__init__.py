import datetime
import decimal

from flask_security.confirmable import generate_confirmation_link

from flask import Flask, json
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_oauthlib.provider import OAuth2Provider
from flask_security.utils import hash_password
from flask_app.app.config import Config
from flask_app.app.database import db, ma
from flask_security import Security
from flask_app.app.database.models import user_datastore, Client
from flask_security.mail_util import MailUtil
from flask_mail import Mail, Message
from flask_login import LoginManager

from flask_security import AnonymousUser
from flask_security.core import (
    _user_loader as _flask_security_user_loader,
    _request_loader as _flask_security_request_loader)
from flask_security.utils import config_value as security_config_value

oauth = OAuth2Provider()

def _request_loader(request):
    """
    Load user from OAuth2 Authentication header or using
    Flask-Security's request loader.
    """
    user = None

    if hasattr(request, 'oauth'):
        user = request.oauth.user
    else:
        # Need this try stmt in case oauthlib sometimes throws:
        # AttributeError: dict object has no attribute startswith
        try:
            is_valid, oauth_request = oauth.verify_request(scopes=[])
            if is_valid:
                user = oauth_request.user
        except AttributeError:
            pass

    if not user:
        user = _flask_security_request_loader(request)

    return user

def _get_login_manager(app, anonymous_user):
    """Prepare a login manager for Flask-Security to use."""
    login_manager = LoginManager()

    login_manager.anonymous_user = anonymous_user or AnonymousUser
    login_manager.login_view = '{0}.login'.format(
        security_config_value('BLUEPRINT_NAME', app=app))
    login_manager.user_loader(_flask_security_user_loader)
    login_manager.request_loader(_request_loader)

    if security_config_value('FLASH_MESSAGES', app=app):
        (login_manager.login_message,
         login_manager.login_message_category) = (
            security_config_value('MSG_LOGIN', app=app))
        (login_manager.needs_refresh_message,
         login_manager.needs_refresh_message_category) = (
            security_config_value('MSG_REFRESH', app=app))
    else:
        login_manager.login_message = None
        login_manager.needs_refresh_message = None

    login_manager.init_app(app)
    return login_manager


_LEVELLOG_ = 20
cors = CORS()
jwt = JWTManager()
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


    app.json_encoder = JSONEncoder
    jwt.init_app(app)
    cors.init_app(app)
    mail.init_app(app)
    security.init_app(
                app, user_datastore,
                login_manager=_get_login_manager(app, anonymous_user=None))
    from flask_app.app.namespaces import managment
    import flask_app.app.cli as cli 
    app.register_blueprint(managment)
    app.register_blueprint(cli.gen)

    @app.before_first_request
    def create_first_user():
        if not user_datastore.find_user(email="tjimenezsblanca@gmail.com"):
            firstuser = user_datastore.create_user(email="tjimenezsblanca@gmail.com", username='ToniJSB', name='ToniJSB', password=hash_password("ToniJSB"))
            adminrole = user_datastore.create_role(name='Admin', permissions='can_create_users, can_delete_users')
            user_datastore.add_role_to_user(firstuser, adminrole)
            user_datastore.commit()

    @oauth.clientgetter
    def load_client(client_id):
        return Client.query.filter_by(Client.id == client_id).first()

    return app


app = create_app()
