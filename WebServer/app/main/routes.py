from flask import make_response
from app.main import bp

print("Importing main")

@bp.route('/database', methods=['GET'])
def view_database():
    print("entering db method")
    return ("Hello World", 200)
