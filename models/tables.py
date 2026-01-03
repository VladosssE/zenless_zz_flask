from extensions import db
from sqlalchemy import text


class Bangboo_stats(db.Model):
    __tablename__ = 'bangboo_stats_zzz'
    bangboo_id = db.Column(db.Integer, primary_key=True)
    bangboo_name = db.Column(db.String(250), nullable=False)
    bangboo_level = db.Column(db.Integer)
    bangboo_stars = db.Column(db.Integer)
    bangboo_class = db.Column(db.String(1))
    bangboo_image_url = db.Column(db.String(100))


class Character_stats(db.Model):
    __tablename__ = 'characters_stats_zzz'
    character_id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(250))
    character_type = db.Column(db.String(250))
    character_class = db.Column(db.String(1))
    character_level = db.Column(db.Integer)
    character_mental_picture = db.Column(db.Integer)
    character_skill_1 = db.Column(db.Integer)
    character_skill_2 = db.Column(db.Integer)
    character_skill_3 = db.Column(db.Integer)
    character_skill_4 = db.Column(db.Integer)
    character_skill_5 = db.Column(db.Integer)
    character_skill_strength = db.Column(db.String(1))
    character_disk_1 = db.Column(db.Integer)
    character_disk_2 = db.Column(db.Integer)
    character_disk_3 = db.Column(db.Integer)
    character_disk_4 = db.Column(db.Integer)
    character_disk_5 = db.Column(db.Integer)
    character_disk_6 = db.Column(db.Integer)
    character_amplificator_unique = db.Column(db.String(3))
    character_amplificator_level = db.Column(db.Integer)
    character_amplificator_stars = db.Column(db.Integer)
    character_image_url = db.Column(db.String(100))


class Godfinger_stats(db.Model):
    __tablename__ = 'godfinger_stats_zzz'
    godfinger_id = db.Column(db.Integer, primary_key=True)
    godfinger_game = db.Column(db.String(125))
    godfinger_medal_icon = db.Column(db.String(125))
    godfinger_ach_name = db.Column(db.String(150))
    godfinger_ach_desc = db.Column(db.String(400))
    godfinger_award = db.Column(db.Integer)
    godfinger_status = db.Column(db.String(12))


class Mewmew_stats(db.Model):
    __tablename__ = 'mewmew_stats_zzz'
    mew_id = db.Column(db.Integer, primary_key=True)
    mew_street = db.Column(db.String(100))
    mew_name = db.Column(db.String(100))
    mew_desc = db.Column(db.String(300))
    mew_status = db.Column(db.String(12))
