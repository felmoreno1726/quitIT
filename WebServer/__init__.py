from flask import Flask
#from app.database import DB
from flask_migrate import Migrate
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy


def register_blueprints(app):
    """
    Calls the different modules of the server to initialize them
    """

app = Flask(__name__)
logger = app.logger
#socketio = SocketIO(app, logger=logger)
#Shows devices currently logged in to the system
session = {}

app = Flask(__name__)


app.config['SECRET_KEY'] ='QIeUZCKK4niYcHSD4cFh8RNhjfMcYO-b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ccbeovms:QIeUZCKK4niYcHSD4cFh8RNhjfMcYO-b@salt.db.elephantsql.com:5432/ccbeovms'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(100), nullable=False)
    coordinates = db.Column(db.String(100))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),nullable=False )
    coordinates = db.Column(db.String(20))
    phone_number = db.Column(db.String(20),nullable=False )

register_blueprints(app)
