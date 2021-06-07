from flask_app.app.database.models import PostComment, PostLikes
import flask_app.app.database.dao.commentDao as dao


def create_comment(creator, post_id, bodyPost):
    comment = PostComment()
    comment.message = message
    comment.post_id = post_id
    comment.created_by_fk = creator
    
    dao.generate_commentPost(comment)

    return {
        'error_type': 'positive',
        'error_desc': 'Mensaje añadido correctamente'
    }


def get_post_comments(post_id):
    commentsList = dao.find_comments_by_post_id(post_id)

    return commentsList