
import flask
from application import app, db
from application.models import User,UserEncoder
import json

from flask import abort


@app.route('/api/v1.0/user/', methods=['GET'])
def get_user():
    users = User.query.all()
    return flask.jsonify({'users': users})


@app.route('/api/v1.0/user/<int:user_id>', methods=['GET'])
def user(user_id):
    user = list(User.query.filter_by(id=user_id))
    if len(user) == 0:
        abort(404)
    return json.dumps(user[0], cls=UserEncoder)