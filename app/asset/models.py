from app import db
from datetime import datetime

class Transaction(db.Model):
    __tablename__ = 'transaction'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False)
    asset_name = db.Column(db.String(100), nullable=False, index=True)
    person_name = db.Column(db.String(100))
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    status = db.Column(db.String(50))

    def __init__(self, type, asset_name, person_name, start_time, end_time, status):
        self.type = type
        self.asset_name = asset_name
        self.person_name = person_name
        self.start_time = start_time
        self.end_time = end_time
        self.status = status

    def __repr__(self):
        return '{} by {}'.format(self.asset_name, self.person_name)