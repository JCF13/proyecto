from backend.flask_app.app.database.models import PostComment, PostLikes
import backend.flask_app.app.database.dao.commentDao as dao


def create_comment(creator, post_id, message):
    comment = PostComment()
    comment.message = message
    comment.post_id = post_id
    comment.created_by_fk = creator

    return {
        'error_type': 'positive',
        'error_desc': 'Mensaje añadido correctamente',
        'message': dao.generate_commentPost(comment)
    }


def get_post_comments(post_id):
    commentsList = dao.find_comments_by_post_id(post_id)

    return commentsList