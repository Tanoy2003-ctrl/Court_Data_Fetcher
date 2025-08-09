from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class QueryLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    case_type = db.Column(db.String(50))
    cnr_number = db.Column(db.String(25))
    filing_year = db.Column(db.String(4))
    response_html = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)