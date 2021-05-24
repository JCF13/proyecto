from flask_app.app.database.models import PostComment
import flask_app.app.database.dao.commentDao as dao


def generate_comment(creator, postId, bodyPost):
    comment = PostComment()
    comment.message = bodyPost.get('message')
    # post.post_id = bodyPost.get('id')
    comment.post_id = postId
    comment.created_by_fk = creator
    dao.create_commentPost(comment)


def get_post_comments(post_id):
    commentsList = dao.find_comments_by_post_id(post_id)

    return commentsList
