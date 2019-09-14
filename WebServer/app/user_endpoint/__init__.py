from flask import Blueprint
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from app.user_endpoint import routes

bp = Blueprint('devices', __name__, url_prefix="/device")
app = Flask(__name__, static_folder='./static')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

bp = Blueprint('devices', __name__, url_prefix="/user_endpoint")



