# -*- coding: utf-8 -*-
from flask import *
from werkzeug.urls import url_parse

from application import app
from application.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'SaNya'}
    return render_template('index.html', user = user ,title='Home Page')



