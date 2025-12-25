from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()

class Bangboo_stats(db.Model):
    __tablename__ = 'bangboo_stats_zzz'
    bangboo_id = db.Column(db.Integer, primary_key=True)
    bangboo_name = db.Column(db.String(250), nullable=False)
    bangboo_level = db.Column(db.Integer)
    bangboo_stars = db.Column(db.Integer)
    bangboo_class = db.Column(db.String(1))
    bangboo_image_url = db.Column(db.String(100), server_default=text("'no_picture.png'"))
