from flask import make_response, render_template
from app.main import bp



main_namespace = "/"

@bp.route('/')
def view_database():
    print("What's wrong")
    return render_template("home.html")

