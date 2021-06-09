import base64
from datetime import datetime
import os

from flask.globals import current_app
from sqlalchemy.sql.expression import false, true
from flask_app.app.database.schemas import PostSchema
from flask_app.app.database.models import Post, PostLikes
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
            'error_type': 'positive',
            'error_desc': 'Publicación creada correctamente'
        }
    except:
        raise Exception


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
            'error_type': 'positive',
            'error_desc': 'Has indicado que te gusta esta publicación'
        }
    else:
        return {
            'error_type': 'warning',
            'error_desc': 'Ya has indicado que te gusta esta publicación'
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
            'error_type': 'positive',
            'error_desc': 'Post eliminado correctamente'
        }
    else:
        return {
            'error_type': 'error',
            'error_desc': 'Ha ocurrido un error'
        }