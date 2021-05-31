from flask_app.app.services.utils import save_file
from os import execlp
from flask_app.app.database.models import ChatImage, PostImage, ProfileImage
import flask_app.app.database.dao.imageDao as dao

def save_picture(picture, name):
    picture_path = os.path.join(current_app.root_path, 'app\\static\\uploads', name+'.png')
    try:
        with open(picture_path, 'xb') as img:
            img.write(base64.b64decode(picture))
        return picture_path
    except:
        raise Exception()

def create_post_image(image,  user_id):

def get_picture(path):
    with open(path, 'rb') as img:
        pic = base64.b64encode(img.read())
        return {
            'picture': pic
        }

    try:
        dao.generate_image(objImage)
    except Exception as exc:
        raise exc
    pass


def create_profile_image(image):
    try:
        raw_file_name = dao.find_last_profile_image()
        objImage = ProfileImage()
        objImage.image = image
        profile_file_name = 'picture_' + str(raw_file_name)
        save_file(image, profile_file_name, '.png')

        dao.generate_image(objImage)
    except Exception as exc:
        raise exc
    pass

def create_chat_image(image,  user_id):
    objImage = ChatImage()
    objImage.image = image

    try:
        dao.generate_image(objImage)
    except Exception as exc:
        raise exc
    pass


def create_image(image, kind: str, user_id=1):
    if kind == 'post':
        create_post_image(image, user_id)
    if kind == 'profile':
        create_profile_image(image)
    if kind == 'chat':
        create_chat_image(image, user_id)
    
    pass