from getpass import getpass
import click
from flask import current_app
from flask.cli import with_appcontext
from flask_app.app.database import db
import flask_app.app.database.models as models

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
    first_name = input('first name: ')
    last_name = input('last name: ')
    password = getpass('password: ')
    confirm_password = getpass('confirm password: ')

    if password == confirm_password:
        hashed_pass = bcrypt.generate_password_hash(password).decode('utf-8')
        user = Usuario(username=username,first_name=first_name,last_name=last_name,password=hashed_pass)
        
        ownId = db.engine.execute('select max(id) from usuario')
        laid = [row[0] for row in ownId]
        
        if laid[0] == None:
            laid[0] = 0

        user.created_by_fk = laid[0] + 1
        user.changed_by_fk = laid[0] + 1
        db.session.add(user)
        db.session.commit()
