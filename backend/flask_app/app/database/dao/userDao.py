from backend.flask_app.app.database.models import User
from backend.flask_app.app.database import db


def find_user_by_username(username: str):
    return User.query.filter(User.username == username).first()


def find_user_by_email(email: str):
    return User.query.filter(User.email == email).first()


def generate_user(user: User):
    db.session.add(user)
    db.session.commit()
