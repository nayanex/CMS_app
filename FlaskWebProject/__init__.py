"""
The flask application package.
"""
import logging
import sys

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from config import Config
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
# TODO: Add any logging levels and handlers with app.logger
logging_dict = {
    "version": 1,
    "formatters": {
        "default": {
            "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
        }
    },
}

logging.config.dictConfig(logging_dict)
MIN_LOGGING_LEVEL = logging.INFO
app.logger.setLevel(logging.INFO)

stdout_stream_handler = logging.StreamHandler(stream=sys.stdout)
stderr_stream_handler = logging.StreamHandler(stream=sys.stderr)

# messages lower than WARNING go to stdout
# messages >= WARNING go to stderr
stdout_stream_handler.setLevel(MIN_LOGGING_LEVEL)
stderr_stream_handler.setLevel(logging.WARNING)

app.logger.addHandler(stdout_stream_handler)
app.logger.addHandler(stderr_stream_handler)

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = "login"

import FlaskWebProject.views
