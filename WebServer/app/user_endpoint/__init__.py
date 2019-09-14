from flask import Blueprint

bp = Blueprint('devices', __name__, url_prefix="/user_endpoint")
from app.user_endpoint import routes
