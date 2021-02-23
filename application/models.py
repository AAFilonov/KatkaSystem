from application import db, login
import werkzeug.security as security
import flask_login



class User(flask_login.UserMixin, db.Model):
    # статические константы для опредления классов
    ROLE_USER = 1
    ROLE_ADMIN = 2

    # поля класса
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.Integer)

    def is_admin(self):
        return self.role == User.ROLE_ADMIN

    def set_password(self, password):
        self.password_hash = security.generate_password_hash(password)

    def check_password(self, password):
        return security.check_password_hash(self.password_hash, password)


    def __repr__(self):
        return '<User {}>'.format(self.username)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


@login.request_loader
def load_user(request):
    token = request.headers.get('Authorization')
    if token is None:
        token = request.args.get('token')

    if token is not None:
        username, password = token.split(":")  # naive token
        user_entry = User.get(username)
        if (user_entry is not None):
            user = User(user_entry[0], user_entry[1])
            if (user.password == password):
                return user
    return None


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    body = db.Column(db.String(140))
    bio = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
