from flask import Blueprint
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

bp = Blueprint('user_endpoint', __name__, url_prefix="/user_endpoint")

from app.user_endpoint import routes
