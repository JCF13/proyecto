from getpass import getpass
import click
from flask import current_app
from flask.cli import with_appcontext
from backend.flask_app.app import bcrypt
from backend.flask_app.app.database import db
from backend.flask_app.app.database.models import User

@click.command(name='database')
@with_appcontext
def create_db():
    """ Create the database"""

    db.create_all()


@click.command(name='admin')
@with_appcontext
def create_admin():
    """Create an Admin user for the database"""
    username = input('username: ')
    name = input('first name: ')
    email = input('email: ')
    password = getpass('password: ')
    confirm_password = getpass('confirm password: ')

    if password == confirm_password:
        hashed_pass = bcrypt.generate_password_hash(password).decode('utf-8')
        print(User.__dict__)
        user = User(username = username,name=name,email=email,password=hashed_pass)
        # user.username = username
        # user.name=name
        # user.surname=surname
        # user.email=email
        # user.password=hashed_pass
        print(user.__dict__)
        db.session.add(user)
        db.session.commit()
