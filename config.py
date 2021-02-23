import os

basedir = os.path.abspath(os.path.dirname(__file__))
DB_USER = 'ubuntudev'
DB_PASS = 'aveemperor1'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = '/test_db'


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              "postgresql://" + DB_USER + ":" + DB_PASS + '@' + DB_HOST + ':' + DB_PORT + DB_NAME
    SQLALCHEMY_TRACK_MODIFICATIONS = False



