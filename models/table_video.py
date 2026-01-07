from extensions import db

class Video_stats(db.Model):
    __tablename__ = 'videoarchive_stats_zzz'
    video_id = db.Column(db.Integer, primary_key=True)
    video_path = db.Column(db.String(25))
    video_chapter = db.Column(db.String(50))
    video_status = db.Column(db.String(11))
