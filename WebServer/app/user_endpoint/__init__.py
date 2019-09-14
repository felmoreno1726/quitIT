from flask import Blueprint

bp = Blueprint('user_endpoint', __name__, url_prefix="/user_endpoint")
from app.user_endpoint import routes
