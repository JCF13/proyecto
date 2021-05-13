from flask_app.app.database.schemas import PostSchema
from flask_app.app.namespaces.private.schemas import postModel
import flask_app.app.database.dao.postDao as dao

def get_all_posts():
    return dao.find_all_posts()

# def generate_post(post):
    