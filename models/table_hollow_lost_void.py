from extensions import db

class Hollow_lost_void_stats(db.Model):
    __tablename__ = 'hollow_lost_void_stats_zzz'
    hollow_lv_id = db.Column(db.Integer, primary_key=True)
    hollow_lv_section = db.Column(db.String(50))
    hollow_lv_name = db.Column(db.String(50))
    hollow_lv_url = db.Column(db.String(15))
    hollow_lv_status = db.Column(db.String(11))
