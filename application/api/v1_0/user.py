import flask
from application import app
import application.Models.m_user  as m_user
import json
from flask import abort, jsonify, make_response

User = m_user.User


@app.route('/api/v1.0/user/', methods=['GET'])
def get_users():
    users_obj = list(User.query.all())
    users = [usr.serialize() for usr in users_obj]
    print(users)
    # json.dumps(users_obj.serialize(), sort_keys=True)
    return {'users': users}


@app.route('/api/v1.0/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = list(User.query.filter_by(id=user_id))
    if len(user) == 0:
        # abort(404)
        return make_response(jsonify({'error': 'Not found'}), 404)
    return user[0].serialize()
