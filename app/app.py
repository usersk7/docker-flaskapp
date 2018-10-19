from typing import List, Dict
from flask import Flask
import mysql.connector
import json
from flask import Flask, flash, redirect, render_template, request, session, abort
import os


app = Flask(__name__)


def employee() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'knights'
        
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM emp')
    data = cursor.fetchall()
    cursor.close()
    connection.close()

    return data

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!  <a href='/logout'>Logout</a>"

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()



@app.route('/show')
def index() -> str:
   return json.dumps({'Employee': employee()})



if __name__ == '__main__':
    app.run(host='0.0.0.0')

