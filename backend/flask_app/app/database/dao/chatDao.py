from backend.flask_app.app.database.models import Chat
from backend.flask_app.app.database import db
from sqlalchemy import or_

def generate_chat(chat: Chat):
    db.session.add(chat)
    db.session.flush()
    db.session.commit()
    return chat.partner_id


def find_by_user_id(user_id: int):
    return Chat.query.filter((Chat.created_by_fk==user_id) or (Chat.partner_id==user_id)).all()


def find_by_users(user_id: int, partner_id: int):
    return Chat.query.filter((Chat.created_by_fk==user_id and Chat.partner_id==partner_id) or 
        (Chat.created_by_fk==partner_id and Chat.partner_id==user_id)).first()