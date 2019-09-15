from app import db

class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(100), nullable=False)
    coordinates = db.Column(db.String(100))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),nullable=False )
    coordinates = db.Column(db.String(20))
    phone_number = db.Column(db.String(20))
