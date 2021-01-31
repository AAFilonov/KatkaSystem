# -*- coding: utf-8 -*-
from flask import *
from werkzeug.urls import url_parse

from application import app
from application.forms import LoginForm
import application.database as db

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'test'}
    database = db.db_open()
    db_cursor = database.cursor()
    db_cursor.execute('SELECT 1')
    records = db_cursor.fetchall()
    db_cursor.close()

    return render_template('index.html', user = user , data = repr(records), title='Home Page')



