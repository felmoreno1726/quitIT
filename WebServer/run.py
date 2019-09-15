from app import app, socketio
from flask_socketio import SocketIO

socketio.run(app, host="127.0.0.1", port=5000, debug=True)

if __name__ == '__main__':
    app.run()