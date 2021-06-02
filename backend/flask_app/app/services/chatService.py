from backend.flask_app.app.database.dao.chatDao import generate_chat, find_by_user_id, find_by_users
from backend.flask_app.app.database.models import Chat

def create_chat(user_id, partner_id):
    if user_id != partner_id:
        chat = Chat(created_by_fk=user_id, partner_id=partner_id)
        return {
            'type': 'positive',
            'message': 'Chat creado',
            'partner_id': generate_chat(chat)
        }

    return {
        'type': 'negative',
        'message': 'Es tu propio perfil'
    }


def get_chats_by_user(user_id):
    print(user_id)
    return find_by_user_id(user_id)


def get_chat_by_users(user_id, partner_id):
    return find_by_users(user_id, partner_id)