import datetime
import decimal
import os
from flask import Flask, json
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_app.app.config import Config

cors = CORS()
marsh = Marshmallow()
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

    from flask_app.app.database import db
    db.init_app(app)
    app.json_encoder = JSONEncoder
    cors.init_app(app)
    marsh.init_app(app)
    from flask_app.app.namespaces import managment
    import flask_app.app.cli as cli 
    app.register_blueprint(managment)
    app.register_blueprint(cli.gen)
    

    return app

app = create_app()