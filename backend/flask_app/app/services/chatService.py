from flask import json
from backend.flask_app.app.database.schemas import ChatMessageSchema
from datetime import datetime
from backend.flask_app.app.database.dao.chatDao import generate_chat, find_by_user_id, find_by_users, new_message
from backend.flask_app.app.database.models import Chat, ChatMessages

def create_chat(user_id, partner_id):
    if user_id != partner_id:
        chat = get_chat_by_users(user_id, partner_id)

        if chat is None:
            chat = Chat(created_by_fk=user_id, partner_id=partner_id)
            return {
                'type': 'positive',
                'message': 'Chat creado',
                'partner_id': generate_chat(chat)
            }
        else:
            return {
                'type': 'warning',
                'message': '',
                'partner_id': partner_id
            }

    return {
        'type': 'negative',
        'message': 'Es tu propio perfil'
    }


def get_chats_by_user(user_id):
    return find_by_user_id(user_id)


def get_chat_by_users(user_id, partner_id):
    return find_by_users(user_id, partner_id)


def send_message(created_by, chat_id, message_text):
    my_message = ChatMessages()
    my_message.message = message_text
    my_message.chat_id = chat_id
    my_message.created_by_fk = created_by
    my_message.created_on = datetime.now()
    
    message = new_message(my_message)

    print(message.message)
    
    return {
        'type': 'positive',
        'message': 'Enviado',
        'new_message': {
            'created_on': str(message.created_on),
            'created_by': message.created_by_fk,
            'message': message.message,
            'message_id': message.message_id
        }
    }