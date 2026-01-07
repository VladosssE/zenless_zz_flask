from extensions import db

class Mewmew_stats(db.Model):
    __tablename__ = 'mewmew_stats_zzz'
    mew_id = db.Column(db.Integer, primary_key=True)
    mew_street = db.Column(db.String(100))
    mew_name = db.Column(db.String(100))
    mew_desc = db.Column(db.String(300))
    mew_status = db.Column(db.String(12))
