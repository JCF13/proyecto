import base64
from flask.globals import current_app
from backend.flask_app.app.services.utils import save_file
from os import execlp
import backend.flask_app.app.database.dao.imageDao as dao
import os
import base64

def save_picture(picture, name):
    picture_path = os.path.join(current_app.root_path, 'app\\static\\uploads', name+'.png')
    try:
        with open(picture_path, 'xb') as img:
            img.write(base64.b64decode(picture))
        return picture_path
    except:
        raise Exception()


def get_picture(path):
    with open(path, 'rb') as img:
        pic = base64.b64encode(img.read())
        return {
            'picture': pic
        }