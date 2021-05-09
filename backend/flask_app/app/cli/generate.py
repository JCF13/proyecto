from getpass import getpass
import click
from flask import current_app
from flask.cli import with_appcontext
from backend.flask_app.app.database import db
from backend.flask_app.app import bcrypt
import backend.flask_app.app.database.models as models

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
    surname = input('last name: ')
    password = getpass('password: ')
    confirm_password = getpass('confirm password: ')

    if password == confirm_password:
        hashed_pass = bcrypt.generate_password_hash(password).decode('utf-8')
        user = models.User(username=username,name=name,surname=surname,password=hashed_pass)
        
        ownId = db.engine.execute('select max(id) from usuario')
        laid = [row[0] for row in ownId]
        
        if laid[0] == None:
            laid[0] = 0

        user.created_by_fk = laid[0] + 1
        
        db.session.add(user)
        db.session.commit()
