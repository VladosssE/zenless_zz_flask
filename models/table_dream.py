from extensions import db

class Dream_stats(db.Model):
    __tablename__ = 'dream_stats_zzz'
    dream_id = db.Column(db.Integer, primary_key=True)
    dream_section = db.Column(db.String(20))
    dream_name = db.Column(db.String(25))
    dream_status = db.Column(db.String(12))
