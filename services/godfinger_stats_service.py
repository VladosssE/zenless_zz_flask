from extensions import db
from models.tables import Godfinger_stats
from sqlalchemy import func

class GodfingerService:

    @staticmethod
    def get_all():
        return Godfinger_stats.query.order_by(Godfinger_stats.godfinger_id).all()

    @staticmethod
    def toggle_status(godfinger_id):
        godfinger = Godfinger_stats.query.get_or_404(godfinger_id)
        
        if godfinger.godfinger_status == "Выполнено":
            godfinger.godfinger_status = "Не выполнено"
        else:
            godfinger.godfinger_status = "Выполнено"

        db.session.commit()

    @staticmethod
    def get_by_game(game):
        return Godfinger_stats.query.filter_by(
            godfinger_game=game
        ).order_by(Godfinger_stats.godfinger_id).all()

    @staticmethod
    def get_all_games():
        return(
            db.session.query(Godfinger_stats.godfinger_game)
            .distinct()
            .order_by(Godfinger_stats.godfinger_game)
            .all()
            )
    
    @staticmethod
    def achievements_summary():
        games = [g[0] for g in Godfinger_stats.query.with_entities(Godfinger_stats.godfinger_game).distinct()]
        summary = {}
        for game in games:
            total = Godfinger_stats.query.filter_by(godfinger_game=game).count()
            completed = Godfinger_stats.query.filter_by(godfinger_game=game, godfinger_status="Выполнено").count()
            summary[game] = {"completed": completed, "total": total}
        return summary

    @staticmethod
    def total_completed():
        completed = Godfinger_stats.query.filter_by(godfinger_status="Выполнено").count()
        total = Godfinger_stats.query.count()
        return {"completed": completed, "total": total}

    @staticmethod
    def update(godfinger_id, status):
        godfinger = Godfinger_stats.query.get_or_404(godfinger_id)

        godfinger.godfinger_status = str(status)

        db.session.commit()
