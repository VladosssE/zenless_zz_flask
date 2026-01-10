from extensions import db

class Events_stats(db.Model):
    __tablename__ = 'events_stats_zzz'
    events_id = db.Column(db.Integer, primary_key=True)
    events_version = db.Column(db.String(5))
    events_start_date = db.Column(db.Date)
    events_end_date = db.Column(db.Date)
    events_name = db.Column(db.String(100))
    events_picture = db.Column(db.String(20))
    events_status = db.Column(db.String(11))
