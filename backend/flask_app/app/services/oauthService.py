from flask_app.app.database.models import Client, Token
from flask_app.app.database.dao.oauthDao import (
    find_token_by_accs_tok, find_token_by_cli_and_user,
    find_token_by_ref_tok, generate_token, find_client_by_id
    )


def create_token(token, expires, request):
    tok = Token(
        access_token=token['access_token'],
        refresh_token=token['refresh_token'],
        token_type=token['token_type'],
        _scopes=token['scope'],
        expires=expires,
        client_id=request.client.client_id,
        user_id=request.user.id,
    )
    generate_token(tok)
    pass


def get_tokens(request_info):
    token = find_token_by_cli_and_user(request_info.client.client_id, request_info.user.id)
    return token


def get_token_by_accs_tok(access_tok):
    token = find_token_by_accs_tok(access_tok)
    return token


def get_token_by_ref_tok(ref_tok):
    token = find_token_by_ref_tok(ref_tok)
    return token


def get_client_by_id(client_id):
    token = find_client_by_id(client_id)
    return token

