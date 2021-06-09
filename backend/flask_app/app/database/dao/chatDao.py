from backend.flask_app.app.database.models import Chat, ChatMessages
from backend.flask_app.app.database import db
from sqlalchemy import or_

def generate_chat(chat: Chat):
    db.session.add(chat)
    db.session.flush()
    db.session.commit()
    return chat.partner_id


def find_by_user_id(user_id: int):
    return Chat.query.filter((Chat.created_by_fk==user_id) | (Chat.partner_id==user_id)).all()


def find_by_users(user_id: int, partner_id: int):
    return Chat.query.filter(((Chat.created_by_fk==user_id) & (Chat.partner_id==partner_id)) | 
        ((Chat.created_by_fk==partner_id) & (Chat.partner_id==user_id))).first()


def new_message(message: ChatMessages):
    db.session.add(message)
    db.session.flush()
    db.session.commit()
    return message


def delete(chat: Chat):
    db.session.delete(chat)
    db.session.commit()


def find_by_id(chat_id: int):
    return Chat.query.filter(Chat.chat_id==chat_id).first()