from flask import Blueprint
from backend.flask_app.app.cli.generate import create_admin, create_db

gen = Blueprint('gen',__name__,cli_group='generate')
gen.cli.add_command(create_db)
gen.cli.add_command(create_admin)
