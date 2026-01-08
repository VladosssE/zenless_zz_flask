from extensions import db

class Hdd_stats(db.Model):
    __tablename__ = 'hdd_stats_zzz'
    hdd_id = db.Column(db.Integer, primary_key=True)
    hdd_order = db.Column(db.Integer)
    hdd_chapter = db.Column(db.String(100))
    hdd_subchapter = db.Column(db.String(50))
    hdd_dif = db.Column(db.String(22))
    hdd_subname = db.Column(db.String(20))
    hdd_url = db.Column(db.String(15))
    hdd_name = db.Column(db.String(50))
    hdd_status = db.Column(db.String(11))
