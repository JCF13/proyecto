from backend.flask_app.app.database.models import PostComment, PostLikes
import backend.flask_app.app.database.dao.commentDao as dao


def create_comment(creator, postId, bodyPost):
    comment = PostComment()
    comment.message = message
    comment.post_id = post_id
    comment.created_by_fk = creator
    
    dao.generate_commentPost(comment)

    return {
        'type': 'positive',
        'message': 'Mensaje añadido correctamente'
    }


def get_post_comments(post_id):
    commentsList = dao.find_comments_by_post_id(post_id)

    return commentsList