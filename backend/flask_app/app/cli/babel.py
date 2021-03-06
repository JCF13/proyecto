import os
import click
from flask.cli import with_appcontext


@click.command(name='extract')
def extract():
    """Extract text from project and create messages.pot."""

    if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
        raise RuntimeError('extract command failed')

@click.command(name='init')
@click.argument('lang')
def init(lang):
    """Initialize a new language."""

    if os.system(
            'pybabel init -i messages.pot -d app/translations -l ' + lang):
        raise RuntimeError('init command failed')

@click.command(name='compile')
def compile():
    """Compile all translations initialized"""
    if os.system('pybabel compile -d app/translations'):
        raise RuntimeError('compile command failed')

@click.command(name='update')
def update():
    """Update messages.pot"""
    if os.system('pybabel update -i messages.pot -d app/translations'):
        raise RuntimeError('update command failed')