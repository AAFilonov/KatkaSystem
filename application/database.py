from flask_sqlalchemy import SQLAlchemy
from config import Config

from urllib.parse import urlparse

db = None


def db_open():
    global db
    if db is None:
        url = Config.DATABASE_URI
        """
        
        dbname = url.path[1:]
        user = url.username
        password = url.password
        host = url.hostname
        port = url.port
        """
        db = psycopg2.connect(url)
        """
        #db = connect(dbname=dbname, user= user,
        #            password=password , host=host, port=port)
        # db = connect(dbname=Config.DB_NAME, user=Config.DB_USER,
        #            password=Config.DB_PASS, host=Config.DATABASE_URI, port=Config.DB_PORT)
        """
    return db
