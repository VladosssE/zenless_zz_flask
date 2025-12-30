from extensions import db
from models.tables import Bangboo_stats

class BangbooService:

    @staticmethod
    def get_all():
        return Bangboo_stats.query.order_by(Bangboo_stats.bangboo_id).all()

    @staticmethod
    def update(bangboo_id, level, stars):
        bangboo = Bangboo_stats.query.get_or_404(bangboo_id)

        bangboo.bangboo_level = int(level)
        bangboo.bangboo_stars = int(stars)

        db.session.commit()
