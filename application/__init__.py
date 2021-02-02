from flask import *
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from application import routes
from application.database import db


# TODO перевод фронтенда на реакт?
# TODO карта с канвасом
