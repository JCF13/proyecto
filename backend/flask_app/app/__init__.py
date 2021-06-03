import datetime
import decimal
from flask import Flask, json
from flask_cors import CORS
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_app.app.config import Config
from flask_app.app.database import db, ma
from flask_app.app.cli.generate import bcrypt

cors = CORS()
jwt = JWTManager()
migrate = Migrate(db=db)


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
    bcrypt.init_app(app)

    from flask_app.app.namespaces import managment
    import flask_app.app.cli as cli 
    app.register_blueprint(managment)
    app.register_blueprint(cli.gen)

    return app


app = create_app()
