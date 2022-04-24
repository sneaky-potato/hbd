from src.models import db

class Birthday(db.Model):
    __tablename__ = 'bdays'

    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    name = db.Column(db.String)
    bday_day = db.Column(db.Integer)
    bday_month = db.Column(db.Integer)