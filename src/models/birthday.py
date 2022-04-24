from src.models import db

class Birthday(db.Model):
    __tablename__ = 'bdays'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    bday = db.Column(db.Date)