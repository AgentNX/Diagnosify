import datetime
from app import db

class SymptomLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symptom = db.Column(db.String(120))
    matched_condition = db.Column(db.String(120))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
