from flask_app.app.services.imageService import get_picture
from flask_app.app.services.userService import get_user_by_id
from flask import json
from flask_app.app.database.schemas import ChatMessageSchema, ChatSchema
from flask.globals import request
from flask_app.app.namespaces.private.schemas import createChat
from flask_app.app.services.logs import complex_file_handler
from flask_jwt_extended import (get_jwt_identity, jwt_required,
                                verify_jwt_in_request)
from flask_restx import Namespace, Resource, marshal
from flask_app.app.services.chatService import create_chat, get_chats_by_user, get_chat_by_users, send_message, delete_chat
from flask_app.app.namespaces.private.schemas import chatModel
from flask_app.app.namespaces.auth.schemas import creator

chat = Namespace('chat', 'Rutas para chats')

chat.logger.addHandler(complex_file_handler)

chat.models[createChat.name] = createChat

parser = chat.parser()

parser.add_argument('Authorization', location='headers', required=True)

@chat.route('/create')
class CreateChat(Resource):
    
    @jwt_required()
    def post(self):
        req_json = request.get_json()

        return create_chat(get_jwt_identity(), req_json['partner_id'])


@chat.route('/getChats')
class GetChats(Resource):

    @jwt_required()
    def get(self):
        chats = get_chats_by_user(get_jwt_identity())
        user_id = get_jwt_identity()
        sqlChat = ChatSchema()

        strChats = sqlChat.dumps(chats, many=True)

        jsonChats = json.loads(strChats)

        for chat in jsonChats:
            if user_id == chat['partner']:
                chat['partner'] = marshal(get_user_by_id(chat['created_by']), creator, skip_none=True)
                chat['partner']['picture'] = str(get_picture(chat['partner']['picture']))
                chat['created_by'] = marshal(get_user_by_id(user_id), creator, skip_none=True)
                chat['created_by']['picture'] = str(get_picture(chat['created_by']['picture']))
            else:
                chat['created_by'] = marshal(get_user_by_id(user_id), creator, skip_none=True)
                chat['created_by']['picture'] = str(get_picture(chat['created_by']['picture']))
                chat['partner'] = marshal(get_user_by_id(chat['partner']), creator, skip_none=True)
                chat['partner']['picture'] = str(get_picture(chat['partner']['picture']))

        return jsonChats


@chat.route('/getChat/<int:partner>')
class GetChat(Resource):

    @jwt_required()
    def get(self, partner):
        user = get_jwt_identity()
        chat = get_chat_by_users(user, partner)

        sqlChat = ChatSchema()
        sqlMessage = ChatMessageSchema()

        strChat = sqlChat.dumps(chat)
        jsonChat = json.loads(strChat)

        strMessage = sqlMessage.dumps(chat.messages, many=True)
        jsonMessages = json.loads(strMessage)
        
        jsonChat['messages'] = jsonMessages
        jsonChat['creator'] = marshal(get_user_by_id(jsonChat['created_by']), creator, skip_none=True)
        jsonChat['creator']['picture'] = str(get_picture(jsonChat['creator']['picture']))
        jsonChat['partner'] = marshal(get_user_by_id(jsonChat['partner']), creator, skip_none=True)
        jsonChat['partner']['picture'] = str(get_picture(jsonChat['partner']['picture']))

        return jsonChat


@chat.route('/newMessage')
class NewMessage(Resource):

    @jwt_required()
    def post(self):
        creator = get_jwt_identity()
        chat_req = request.get_json()

        return send_message(creator, chat_req['chat_id'], chat_req['message'])


@chat.route('/deleteChat')
class DeleteChat(Resource):
    
    @jwt_required()
    def post(self):
        chat_req = request.get_json()

        return delete_chat(chat_req['chat_id'])