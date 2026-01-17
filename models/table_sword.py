from extensions import db

class Sword_stats(db.Model):
    __tablename__ = 'sword_stats_zzz'
    sword_id = db.Column(db.Integer, primary_key=True)
    sword_section = db.Column(db.String(20))
    sword_name = db.Column(db.String(25))
    sword_status = db.Column(db.String(12))