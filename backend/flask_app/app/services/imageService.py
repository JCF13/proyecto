import base64
from flask.globals import current_app
from backend.flask_app.app.services.utils import save_file
from os import execlp
import flask_app.app.database.dao.imageDao as dao
import os
from binascii import Error


def save_picture(picture, name):
    print()
    picture_path = os.path.join(current_app.root_path, 'static\\uploads', name + '.png')
    try:
        with open(picture_path, 'xb') as img:
            img.write(base64.b64decode(picture))
        return picture_path
    except (Error, Exception) as e:
        raise e


def get_picture(path):
    if path is None:
        print('no')
        return 'no hay'
    with open(path, 'rb') as img:
        pic = base64.b64encode(img.read())
        print('si')
        return pic