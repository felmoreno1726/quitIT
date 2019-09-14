from flask import Flask
#from app.database import DB
from flask_socketio import SocketIO


def register_blueprints(app):
    """
    Calls the different modules of the server to initialize them
    """

app = Flask(__name__)
logger = app.logger
socketio = SocketIO(app, logger=logger)
#Shows devices currently logged in to the system
session = {}
register_blueprints(app)
