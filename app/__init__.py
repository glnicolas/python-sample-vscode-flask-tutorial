from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils  import secure_filename
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import os

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your secret key'
    app.config['SECRET_KEY'] = 'its a secret'
    app.config['MYSQL_HOST'] = '192.168.240.176'
    app.config['MYSQL_USER'] = 'admindb'
    app.config['MYSQL_PASSWORD'] = 'CCADT3st1#'
    app.config['MYSQL_DB'] = 'pythonlogin'
    
    SECRET_KEY = "changeme"
    SESSION_TYPE = 'filesystem'
    app.config.from_object(__name__)
    
    from .auth import auth
    from .auth import mysql
    mysql.init_app(app)
    app.register_blueprint(auth)
    app.debug=True
    
    return app