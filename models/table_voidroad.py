from extensions import db

class Voidroad_stats(db.Model):
    __tablename__ = 'voidroad_stats_zzz'
    voidroad_id = db.Column(db.Integer, primary_key=True)
    voidroad_section = db.Column(db.String(20))
    voidroad_name = db.Column(db.String(25))
    voidroad_status = db.Column(db.String(12))