from flask import Blueprint
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from app.user_endpoint import routes

app = Flask(__name__, static_folder='./static')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bp = Blueprint('user_endpoint', __name__, url_prefix="/user_endpoint")

