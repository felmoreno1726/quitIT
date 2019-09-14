from flask import make_response
from app.main import bp


main_namespace = "/"

bp.route('/database', methods=['GET'])
def view_database():
    return make_response("Hello World")
