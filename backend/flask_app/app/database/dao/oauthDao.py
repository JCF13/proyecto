from flask_app.app.database import db
from flask_app.app.database.models import Client, Token

def generate_token(token):
    db.session.add(token)
    db.session.commit()

def find_token_by_cli_and_user(client_id, user_id):
    token = Token.query.filter_by(client_id=client_id,
                                user_id=user_id)
    return token


def find_token_by_accs_tok(access_tok):
    token = Token.query.filter_by(access_token=access_tok)
    return token


def find_token_by_ref_tok(ref_tok):
    token = Token.query.filter_by(refresh_token=ref_tok)
    return token

def find_client_by_id(id):
    token = Token.query.filter_by(client_id=id)
    return token