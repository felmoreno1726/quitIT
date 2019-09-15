from flask import Flask
#from app.database import DB
from flask_migrate import Migrate
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy



def register_blueprints(app):
    """
    Calls the different modules of the server to initialize them
    """
    print("registering blueprints")
    from app.user_endpoint import bp as user_endpoint_bp
    from app.main import bp as main_bp
    app.register_blueprint(user_endpoint_bp)
    app.register_blueprint(main_bp)

app = Flask(__name__)
logger = app.logger
sessions = {
        #username (str): {
            #location: (int, int),
            #phone_number: (str)
            #}
        }
#maps sids to a usernme
sids = {
        #sid (val) : username (str)
        }
app = Flask(__name__)

app.config['SECRET_KEY'] = 'QIeUZCKK4niYcHSD4cFh8RNhjfMcYO-b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ccbeovms:QIeUZCKK4niYcHSD4cFh8RNhjfMcYO-b@salt.db.elephantsql.com:5432/ccbeovms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
socketio = SocketIO(app, logger=logger)
#Session keeps users in the system

db = SQLAlchemy(app)
migrate = Migrate(app, db)
### ALWAYS BE THE LAST LINE
register_blueprints(app)
