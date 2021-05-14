from re import L
from flask_app.app.database.models import User
from flask_app.app.database import db

def find_user_by_username(username:str):
    return User.query.filter(User.username == username).first()

