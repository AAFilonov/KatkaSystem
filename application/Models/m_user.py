from application import db, login
import werkzeug.security as security
import flask_login

import json


class User(flask_login.UserMixin, db.Model):
    """
    Класс-модель для пользователей
    """
    # статические константы для опредления классов
    ROLE_USER = 1
    ROLE_ADMIN = 2

    # поля класса
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.Integer)

    def is_admin(self):
        """
        проверка явялется ли пользователь админом
        """
        return self.role == User.ROLE_ADMIN

    def set_password(self, password):
        """
        заменить пароль
        """
        self.password_hash = security.generate_password_hash(password)

    def check_password(self, password):
        """
        проверить пароль
        """
        return security.check_password_hash(self.password_hash, password)

    @staticmethod
    def deseialize(usr_json):
        """
        десериализовать json
        """
        usr_dict = json.loads(usr_json)
        usr = User.init(

            usr_dict['username'],
            usr_dict['password'],
            usr_dict['id'],
            usr_dict['role']
        )
        return usr

    def serialize(self):
        """
        сериализовать экземпляр в json строку
        """
        return {
            "username": self.username,
            "role": self.role,
            "id": self.id
        }

    @staticmethod
    def init_json(json_str):
        """
        инициализатор по json строке
        """
        usr = User.deseialize(json_str)
        return usr

    @staticmethod
    def init(username, password, id=None, role=ROLE_USER):
        """
        инициализатор всем параметрам
        """
        usr = User(id, username, password,  role)
        return usr

    def __init__(self,id, username, password,  role=ROLE_USER):
        self.id =id
        self.username=username
        self.set_password(password)
        self.role=role

    def __repr__(self):
        return '<User {}>'.format(self.username)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


"""

class UserEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return obj.serialize()
        return super().default(obj)



@login.request_loader
def load_user(request):
    token = request.headers.get('Authorization')
    if token is None:
        token = request.args.get('token')

    if token is not None:
        username, password = token.split(":")  # naive token
        user_entry = User.get(username)
        if user_entry is not None:
            user = User(user_entry[0], user_entry[1])
            if user.password == password:
                return user
    return None
"""
