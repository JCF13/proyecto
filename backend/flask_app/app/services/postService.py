from flask_app.app.database.schemas import PostSchema
from flask_app.app.database.models import Post
from flask_app.app.namespaces.private.schemas import postModel
import flask_app.app.database.dao.postDao as dao

def get_all_posts():
    return dao.find_all_posts()

def generate_post(bodyPost):
        post = Post()
        post.caption = bodyPost.get('caption')
        # post.post_id = bodyPost.get('id')
        post.picture_fname = bodyPost.get('path')
        post.picture_path = bodyPost.get('fname')
        post.created_by_fk = bodyPost.get('user_id')

        dao.create_post(post)