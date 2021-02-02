# -*- coding: utf-8 -*-
from flask import *
from werkzeug.urls import url_parse

from application import app
import application.forms  as Forms
import application.database as db


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'test'}
    database = db.db_open()
    db_cursor = database.cursor()
    db_cursor.execute('SELECT * from users')
    records = db_cursor.fetchall()
    db_cursor.close()

    return render_template('index.html', user=user, data=repr(records), title='Home Page')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Forms.LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)