from extensions import db

class Godfinger_stats(db.Model):
    __tablename__ = 'godfinger_stats_zzz'
    godfinger_id = db.Column(db.Integer, primary_key=True)
    godfinger_game = db.Column(db.String(125))
    godfinger_medal_icon = db.Column(db.String(125))
    godfinger_ach_name = db.Column(db.String(150))
    godfinger_ach_desc = db.Column(db.String(400))
    godfinger_status = db.Column(db.String(12))
