from flask import Blueprint
<<<<<<< HEAD
from flask_app.app.cli.generate import create_admin, create_db
# from flask_app.app.cli.babel import extract,init,update,compile
=======
from backend.flask_app.app.cli.generate import create_admin, create_db
# from backend.flask_app.app.cli.babel import extract,init,update,compile
>>>>>>> pruebas2
gen = Blueprint('gen',__name__,cli_group='generate')
gen.cli.add_command(create_db)
gen.cli.add_command(create_admin)

# translate = Blueprint('trans',__name__,cli_group='babel')
# translate.cli.add_command(extract)
# translate.cli.add_command(init)
# translate.cli.add_command(compile)
# translate.cli.add_command(update)