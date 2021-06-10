from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_security.models import fsqla_v2 as fsqla


db = SQLAlchemy()
ma = Marshmallow()

fsqla.FsModels.set_db_info(db)