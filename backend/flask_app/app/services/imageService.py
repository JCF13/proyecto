from flask_app.app.database.models import ChatImage, PostImage, ProfileImage
import flask_app.app.database.dao.imageDao as dao


def create_post_image(image):
    
    objImage = PostImage()
    pass
def create_profile_image(image):
    
    objImage = ProfileImage()
    pass
def create_chat_image(image):
    
    objImage = ChatImage()
    pass

def create_image(image,user_id, kind: str):
    if kind == 'post':
        create_post_image(image)
    if kind == 'profile':
        create_profile_image(image)
    if kind == 'chat':
        create_chat_image(image)
    
    pass