from extensions import db

class Starhour_stats(db.Model):
    __tablename__ = 'starhour_stats_zzz'
    starhour_id = db.Column(db.Integer, primary_key=True)
    starhour_section = db.Column(db.String(20))
    starhour_name = db.Column(db.String(25))
    starhour_status = db.Column(db.String(12)) 
