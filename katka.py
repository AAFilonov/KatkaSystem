# -*- coding: utf-8 -*-



from config import Config
from contextlib import closing

print("Database opened successfully")
from application import app

if __name__ == "__main__":
    app.run(threaded=True, port=5000)

