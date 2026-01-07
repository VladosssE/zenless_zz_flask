from extensions import db

class Sage_stats(db.Model):
    __tablename__ = 'sage_stats_zzz'
    sage_id = db.Column(db.Integer, primary_key=True)
    sage_street = db.Column(db.String(100))
    sage_time = db.Column(db.String(5))
    sage_url = db.Column(db.String(15))
    sage_location = db.Column(db.String(300))
    sage_status = db.Column(db.String(11))
