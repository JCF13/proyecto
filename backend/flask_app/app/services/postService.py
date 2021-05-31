from flask_app.app.database.schemas import PostSchema
from flask_app.app.database.models import Post
from flask_app.app.services.utils import save_picture
from flask_app.app.namespaces.private.schemas import postModel
import flask_app.app.database.dao.postDao as dao

def get_all_posts():
    return dao.find_all_posts()
    
def get_post_by_id(id):
    return dao.find_post_by_id(id)

def create_post(creator,bodyPost):
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