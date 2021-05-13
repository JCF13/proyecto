from flask_restx import Namespace, fields
from backend.flask_app.app.services.postService import generate_post,get_all_posts

post = Namespace('post','todas las rutas de Posts irán a aquí')

post.add_model('Post',{
'post_id': fields.Integer,
'caption': fields.String,
'picture_path': fields.String,
'picture_fname': fields.String,
'likes': fields.Wildcard,
'comments': fields.,
})