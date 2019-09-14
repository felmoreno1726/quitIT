from app import db


class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(100), nullable=False)
    coordination = db.Column(db.String(100), nullable=False)
