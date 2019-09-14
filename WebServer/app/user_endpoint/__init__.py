from flask import Blueprint

bp = Blueprint('devices', __name__, url_prefix="/device")
from app.devices import routes
