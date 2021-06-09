from backend.flask_app.app.database.models import Post, PostLikes
from backend.flask_app.app.database import db


def generate_post(post: Post):
    """
    Takes a Post object and save it at the data base

    :param post: the actual object which will be
                 saved at the data base
    """
    db.session.add(post)
    db.session.flush()
    db.session.commit()
    
    return post.post_id

    # try:
    #     # for key, val in user.__dict__.items():
    #     #     print('_____________')
    #     #     print(key, '____', val)
    #     #     print('_____________')
    #     print(user.name)
    #     db.session.add(user)
    #     db.session.commit()
    # except IntegrityError as expt:
    #     desglosado = str(expt.orig).split(' ')
    #     fail = desglosado[0]
    #     if fail == 'UNIQUE':
    #         obj_attr = desglosado[3].split('.')
    #         attr = obj_attr

    #         if attr == 'username':
    #             raise UsernameUsed(statement=attr, params=fail, orig=SQLAlchemyError)
    #         elif attr == 'email':
    #             raise EmailUsed(statement=attr, params=fail, orig=SQLAlchemyError)
    #     elif fail == 'NOT':
    #         noNul = str(expt.orig).split(' ')[0] +' '+ str(expt.orig).split(' ')[1]
    #         obj_attr = desglosado[4].split('.')
    #         attr = obj_attr[1]
    #         if attr == 'username':
    #             raise RequiredUsername(statement=attr, params=noNul, orig=SQLAlchemyError)
    #         elif attr == 'name':
    #             raise RequiredName(statement=attr, params=noNul, orig=SQLAlchemyError)
    #         elif attr == 'password':
    #             raise RequiredPassword(statement=attr, params=noNul, orig=SQLAlchemyError)
    #         elif attr == 'email':
    #             raise RequiredEmail(statement=attr, params=noNul, orig=SQLAlchemyError)

    #     raise expt



def find_by_offset(page, users):
    """
    Return all the Post objects of the data base
    """
    ids = []
    for user in users:
        ids.append(user.id)

    return Post.query.filter(Post.created_by_fk.in_(ids)).order_by(Post.created_on).limit(10).offset(page*10)
    #return Post.query.limit(10).offset(page*10)


def find_post_by_id(id):
    """
    Return the Post object wich is identical
    with the param of the data base
    :param id: int
    """
    return Post.query.filter(Post.post_id == id).first()


def find_by_offset_and_followed(page):
    pass


def add_like(like: PostLikes):
    db.session.add(like)
    db.session.commit()


def delete_post(post: Post):
    db.session.delete(post)
    db.session.commit()


def find_like_by_user_and_post(user_id, post_id):
    return PostLikes.query.filter(PostLikes.post_id==post_id, PostLikes.user_id==user_id).first()


def delete_like(like: PostLikes):
    db.session.delete(like)
    db.session.commit()