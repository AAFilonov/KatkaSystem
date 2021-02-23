from unicodedata import UCD

from flask import Flask, jsonify
from application import  app,db
from application.models  import User,UserEncoder
import json

from flask import abort

def make_public_user(user):
    new_user = {}
    for field in user:
       new_user[field] = user[field]
    return new_user


@app.route('/api/v1.0/user/', methods=['GET'])
def get_user():
    users = User.query.all()
    return jsonify({'users': users})


@app.route('/api/v1.0/user/<int:user_id>', methods=['GET'])
def user(user_id):

    user = list(User.query.filter_by(id=user_id))
    if len(user) == 0:
        abort(404)
    return json.dumps(user[0], cls=UserEncoder)