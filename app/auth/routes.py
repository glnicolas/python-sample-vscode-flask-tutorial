from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils  import secure_filename
from flask_mysqldb import MySQL
import MySQLdb.cursors
import json
from . import auth
from . import mysql


@auth.route('/', methods=['GET', 'POST'])
def login():
    print('aqui')
    print(request.method)
    if 'loggedin' in session:
        print('aqui3')
        return render_template('auth/index.html', username=session['username'])
    else:
        if request.method == 'POST' and 'usuario' in request.form and 'password' in request.form:
            username = request.form['usuario']
            password = request.form['password']
            try:
                conn = mysql.connect
                #cursor =conn.cursor()
                cursor =conn.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute(
                    'SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
                account = cursor.fetchone()
                if account:
                    session['loggedin'] = True
                    session['id'] = account['id']
                    session['username'] = account['username']
                    print("aqui2")
                    return redirect(url_for('auth.login'))
            except Exception as e:
                print(e)
                return 'error'
            else:
                msg = 'Incorrect username/password!'
        return render_template('auth/login.html')


@auth.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('auth.login'))
