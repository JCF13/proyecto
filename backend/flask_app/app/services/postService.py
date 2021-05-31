from flask_app.app.database.schemas import PostSchema
from flask_app.app.database.models import Post
from flask_app.app.namespaces.private.schemas import postModel
import flask_app.app.database.dao.postDao as dao

def get_all_posts():
    return dao.find_all_posts()
    
def get_post_by_id(id):
    return dao.find_post_by_id(id)

def create_post(creator,bodyPost):
        post = Post()
        post.caption = bodyPost.get('caption')
        # post.post_id = bodyPost.get('id')
        post.picture = bodyPost.get('path')
        
        post.created_by_fk = creator

        dao.generate_post(post)

def get_comments_by_post():
    return 