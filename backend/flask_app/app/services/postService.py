import base64
from datetime import datetime
import os

from flask.globals import current_app
from flask_app.app.database.schemas import PostSchema
from flask_app.app.database.models import Post
from flask_app.app.namespaces.private.schemas import postModel
import flask_app.app.database.dao.postDao as dao
from flask_app.app.services.imageService import save_picture

def get_by_offset(page, users):
    return dao.find_by_offset(page, users)

    
def get_post_by_id(id):
    return dao.find_post_by_id(id)


def create_post(creator, bodyPost):
    try:
        post = Post()
        post.caption = bodyPost.get('caption')
        post.picture = save_picture(bodyPost.get('picture'), str(creator)+str(datetime.now()).replace(' ', '-').replace('.', '').replace(':', ''))
        post.created_by_fk = creator
        
        return {
            'post_id': dao.generate_post(post),
            'type': 'positive',
            'message': 'Publicación creada correctamente'
        }
    except:
        return {
            'type': 'error',
            'message': 'Ha ocurrido un error'
        }


def get_comments_by_post():
    return 


