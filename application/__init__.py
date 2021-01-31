from flask import *
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from application import routes
from application.database import db


# TODO перевод фронтенда на реакт?
# TODO карта с канвасом
