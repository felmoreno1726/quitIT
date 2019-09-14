from flask import Flask
#from app.database import DB
from flask_socketio import SocketIO

def register_blueprints(app):
    """
    Calls the different modules of the server to initialize them
    """
    from app.user_endpoit import bp as user_endpoint_bp
    app.register_blueprint(user_endpoint_bp)

app = Flask(__name__)
logger = app.logger
socketio = SocketIO(app, logger=logger)
#Session keeps users in the system
sessions = {
        #username (str): {
            #location: (int, int),
            #phone_number: (str)
            #}
        }
#maps sids to a usernme
sids = {
        #sid (val) : 
        }
register_blueprints(app)
