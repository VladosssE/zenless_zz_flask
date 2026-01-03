from flask import Flask, render_template, session
from extensions import db
from models.tables import Bangboo_stats, Character_stats, Godfinger_stats
from routes.bangboo_stats import bp as bangboo_stats_bp
from routes.character_stats import bp as character_stats_bp
from routes.godfinger_stats import bp as godfinger_stats_bp
from routes.mewmew_stats import bp as mew_stats_bp
from models.seed import seed_bangboo, seed_characters, seed_godfinger, seed_mewmew
from services.godfinger_stats_service import GodfingerService
from services.mewmew_stats_service import MewmewService

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///zzz_db.sqlite'
    app.config['SECRET_KEY'] = '0JVJMsRPZunYykzxVfFIhQ'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    with app.app_context():
        db.create_all()
        seed_bangboo()
        seed_characters()
        seed_godfinger()
        seed_mewmew()
        
    app.register_blueprint(bangboo_stats_bp)
    app.register_blueprint(character_stats_bp)
    app.register_blueprint(godfinger_stats_bp)
    app.register_blueprint(mew_stats_bp)
    
    @app.route("/")
    def index():
        total_stats = GodfingerService.total_completed()
        games_list = GodfingerService.get_all_games()
        games_summary = GodfingerService.achievements_summary()

        total_mewmew = MewmewService.total_completed()
        mewmew_list = MewmewService.get_all_streets()
        streets_summary = MewmewService.streets_summary()
        
        return render_template(
            "base.html",
            total_stats=total_stats,
            games_list=[g[0] for g in games_list],
            summary=games_summary,
            total_mewmew=total_mewmew,
            mewmew_list=[l[0] for l in mewmew_list],
            mewmew_summary=streets_summary
        )

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
