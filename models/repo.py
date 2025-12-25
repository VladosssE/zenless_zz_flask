from models.tables import db, Bangboo_stats

class BangbooStatsRepo:
    def __init__(self, db_instance=None):
        if db_instance:
            global db
            db = db_instance

    def all(self):
        return db.session.query(Bangboo_stats).all()

    def add(self, bangboo_name, bangboo_level, bangboo_stars, bangboo_class, image_url):
        new_bangboo = Bangboo_stats(
            bangboo_name = bangboo_name,
            bangboo_level = bangboo_level,
            bangboo_stars = bangboo_stars,
            bangboo_class = bangboo_class,
            image_url = image_url if image_url else None
            )
        db.session.add(new_bangboo)
        db.session.commit()
        return new_bangboo
