from extensions import db
from models.tables import Mewmew_stats
from sqlalchemy import func

class MewmewService:

    @staticmethod
    def get_all():
        return Mewmew_stats.query.order_by(Mewmew_stats.mew_id).all()

    @staticmethod
    def toggle_status(mew_id):
        street = Mewmew_stats.query.get_or_404(mew_id)
        
        if street.mew_status == "Выполнено":
            street.mew_status = "Не выполнено"
        else:
            street.mew_status = "Выполнено"

        db.session.commit()

    @staticmethod
    def get_by_street(street):
        return Mewmew_stats.query.filter_by(
            mew_street=street
        ).order_by(Mewmew_stats.mew_id).all()

    @staticmethod
    def get_all_streets():
        return(
            db.session.query(Mewmew_stats.mew_street)
            .distinct()
            .order_by(Mewmew_stats.mew_street)
            .all()
            )
    
    @staticmethod
    def streets_summary():
        streets = [s[0] for s in Mewmew_stats.query.with_entities(Mewmew_stats.mew_street).distinct()]
        summary = {}
        for street in streets:
            total = Mewmew_stats.query.filter_by(mew_street=street).count()
            completed = Mewmew_stats.query.filter_by(mew_street=street, mew_status="Выполнено").count()
            summary[street] = {"completed": completed, "total": total}
        return summary

    @staticmethod
    def total_completed():
        completed = Mewmew_stats.query.filter_by(mew_status="Выполнено").count()
        total = Mewmew_stats.query.count()
        return {"completed": completed, "total": total}

    @staticmethod
    def update(mew_id, status):
        mews = Mewmew_stats.query.get_or_404(mew_id)

        mews.mew_status = str(status)

        db.session.commit()
