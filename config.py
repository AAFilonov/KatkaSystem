import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'key'
    DATABASE_URI = os.environ.get('DATABASE_URL')
    DB_PORT = 5432
    DB_USER = 'postgres'
    DB_PASS = 'pass'
    DB_NAME = 'test_db'
    #DB_NAME = 'katka_db'
