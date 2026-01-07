from extensions import db

class Friends_stats(db.Model):
    __tablename__ = 'friends_stats_zzz'
    friends_id = db.Column(db.Integer, primary_key=True)
    friends_fraction = db.Column(db.String(100))
    friends_name = db.Column(db.String(100))
    friends_status = db.Column(db.String(20))
