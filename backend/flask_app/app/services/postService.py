import base64
from datetime import datetime
import os

from flask.globals import current_app
from sqlalchemy.sql.expression import false, true
from backend.flask_app.app.database.schemas import PostSchema
from backend.flask_app.app.database.models import Post, PostLikes
from backend.flask_app.app.namespaces.private.schemas import postModel
import backend.flask_app.app.database.dao.postDao as dao
from backend.flask_app.app.services.imageService import save_picture

def get_by_offset(page, users):
    return dao.find_by_offset(page, users)
    
def get_post_by_id(id):
    return dao.find_post_by_id(id)

def generate_post(creator,bodyPost):
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


def new_like(user_id, post_id):
    liked = False
    post = get_post_by_id(post_id)

    for like in post.likes:
        if like.user_id == user_id:
            liked = True
    
    if not liked:
        like = PostLikes(post_id=post_id, user_id=user_id)
        dao.add_like(like)
    
        return {
            'type': 'positive',
            'message': 'Has indicado que te gusta esta publicación'
        }
    else:
        return {
            'type': 'warning',
            'message': 'Ya has indicado que te gusta esta publicación'
        }


def dislike(user_id, post_id):
    like = dao.find_like_by_user_and_post(user_id, post_id)
    dao.delete_like(like)
    
    return {
        'type': 'positive',
        'message': 'Has indicado que ya no te gusta esta publicación'
    }


def delete_post_by_id(post_id):
    post = dao.find_post_by_id(post_id)

    if not post is None:
        dao.delete_post(post)
        
        return {
            'type': 'positive',
            'message': 'Post eliminado correctamente'
        }
    else:
        return {
            'type': 'negative',
            'message': 'Ha ocurrido un error'
        }