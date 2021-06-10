from flask import Blueprint
from flask_mysqldb import MySQL


auth = Blueprint('auth', __name__, template_folder='templates')
mysql = MySQL()

from . import routes
