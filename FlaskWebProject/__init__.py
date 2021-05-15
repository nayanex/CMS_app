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
MIN_LOGGING_LEVEL = logging.INFO
stdout_stream_handler = logging.StreamHandler(sys.stdout)
stderr_stream_handler = logging.StreamHandler(sys.stderr)

# messages lower than WARNING go to stdout
# messages >= WARNING (and >= STDOUT_LOG_LEVEL) go to stderr
stdout_stream_handler.setLevel(MIN_LOGGING_LEVEL)
stdout_stream_handler.setLevel(max(MIN_LOGGING_LEVEL, logging.WARNING))

#rootLogger = logging.getLogger()
#rootLogger.addHandler(stdout_stream_handler)
#rootLogger.addHandler(stdout_stream_handler)
#app.logger = logging.getLogger(__name__)

app.logger.setLevel(logging.INFO)
app.logger.addHandler(stdout_stream_handler)
app.logger.addHandler(stderr_stream_handler)

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = "login"

import FlaskWebProject.views
