from extensions import db

class Summer_stats(db.Model):
    __tablename__ = 'summer_stats_zzz'
    summer_id = db.Column(db.Integer, primary_key=True)
    summer_section = db.Column(db.String(20))
    summer_name = db.Column(db.String(25))
    summer_status = db.Column(db.String(12))
