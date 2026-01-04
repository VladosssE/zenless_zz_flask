from extensions import db
from models.tables import Hdd_stats
from sqlalchemy import func

class HddService:

    @staticmethod
    def get_all():
        return Hdd_stats.query.order_by(Hdd_stats.hdd_id).all()

    @staticmethod
    def toggle_status(hdd_id):
        table = Hdd_stats.query.get_or_404(hdd_id)
        
        if table.hdd_status == "Всё собрано":
            table.hdd_status = "Не пройдено"
        else:
            table.hdd_status = "Всё собрано"

        db.session.commit()

    @staticmethod
    def get_by_chapter(current):
        return Hdd_stats.query.filter_by(
           hdd_chapter=current
        ).order_by(Hdd_stats.hdd_id).all()

    @staticmethod
    def get_all_chapters():
        return(
            db.session.query(Hdd_stats.hdd_chapter)
            .distinct()
            .order_by(Hdd_stats.hdd_chapter)
            .all()
            )
    
    @staticmethod
    def chapters_summary():
        chapters = [c[0] for c in Hdd_stats.query.with_entities(Hdd_stats.hdd_chapter).distinct()]
        summary = {}
        for chapter in chapters:
            total = Hdd_stats.query.filter_by(hdd_chapter=chapter).count()
            completed = Hdd_stats.query.filter_by(hdd_chapter=chapter, hdd_status="Всё собрано").count()
            summary[chapter] = {"completed": completed, "total": total}
        return summary

    @staticmethod
    def total_completed():
        completed = Hdd_stats.query.filter_by(hdd_status="Всё собрано").count()
        total = Hdd_stats.query.count()
        return {"completed": completed, "total": total}

    @staticmethod
    def complete_all():
        Hdd_stats.query.update(
            {"hdd_status": "Всё собрано"}
        )
        db.session.commit()

    @staticmethod
    def update(hdd_id, status):
        hdd = Hdd_stats.query.get_or_404(hdd_id)
        hdd.hdd_status = str(status)
        db.session.commit()
