from extensions import db

class Hollow_withered_domain_stats(db.Model):
    __tablename__ = 'hollow_withered_domain_stats_zzz'
    hollow_wd_id = db.Column(db.Integer, primary_key=True)
    hollow_wd_section = db.Column(db.String(50))
    hollow_wd_name = db.Column(db.String(50))
    hollow_wd_url = db.Column(db.String(15))
    hollow_wd_status = db.Column(db.String(11))
