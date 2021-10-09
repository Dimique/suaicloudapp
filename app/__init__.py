from flask import Flask
from app import config, database

app = Flask(__name__)

config.init_config()
app.config.update(
    CSRF_ENABLED = config.cfg['server']['CSRF_ENABLED'],
    SECRET_KEY = config.cfg['server']['SECRET_KEY']
)

try:
    database.init_db()
    database.init_requests()
except Exception as e:
    print(e)

from app import routes

app.run(
    host = config.cfg['server']['host'], 
    port = config.cfg['server']['port']
)
