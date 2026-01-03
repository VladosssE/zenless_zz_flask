from extensions import db
from models.tables import Sage_stats
from sqlalchemy import func

class SageService:

    @staticmethod
    def get_all():
        return Sage_stats.query.order_by(Sage_stats.sage_id).all()

    @staticmethod
    def toggle_status(sage_id):
        street = Sage_stats.query.get_or_404(sage_id)
        
        if street.sage_status == "Получено":
            street.sage_status = "Не получено"
        else:
            street.sage_status = "Получено"

        db.session.commit()

    @staticmethod
    def get_by_street(street):
        return Sage_stats.query.filter_by(
            sage_street=street
        ).order_by(Sage_stats.sage_id).all()

    @staticmethod
    def get_all_streets():
        return(
            db.session.query(Sage_stats.sage_street)
            .distinct()
            .order_by(Sage_stats.sage_street)
            .all()
            )
    
    @staticmethod
    def streets_summary():
        streets = [s[0] for s in Sage_stats.query.with_entities(Sage_stats.sage_street).distinct()]
        summary = {}
        for street in streets:
            total = Sage_stats.query.filter_by(sage_street=street).count()
            completed = Sage_stats.query.filter_by(sage_street=street, sage_status="Получено").count()
            summary[street] = {"completed": completed, "total": total}
        return summary

    @staticmethod
    def total_completed():
        completed = Sage_stats.query.filter_by(sage_status="Получено").count()
        total = Sage_stats.query.count()
        return {"completed": completed, "total": total}

    @staticmethod
    def update(sage_id, status):
        sage = Sage_stats.query.get_or_404(sage_id)

        sage.sage_status = str(status)

        db.session.commit()
