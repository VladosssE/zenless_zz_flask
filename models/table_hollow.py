from extensions import db

class Hollow_stats(db.Model):
    __tablename__ = 'hollow_stats_zzz'
    hollow_id = db.Column(db.Integer, primary_key=True)
    hollow_name = db.Column(db.String(50))
    hollow_location = db.Column(db.String(50))
    hollow_subname = db.Column(db.String(50))
    hollow_status = db.Column(db.String(11))
