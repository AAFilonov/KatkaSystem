from psycopg2 import *
from config import Config
from contextlib import closing

db = None


def db_open():
    global db
    if db is None:
        db = connect(dbname=Config.DB_NAME, user=Config.DB_USER,
                     password=Config.DB_PASS, host=Config.DATABASE_URI, port=Config.DB_PORT)
    return db
