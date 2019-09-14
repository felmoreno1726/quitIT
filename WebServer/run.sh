from app import app, socketio
from flask_socketio import SocketIO

socketio.run(app, host="0.0.0.0", port=5000, debug=True)
