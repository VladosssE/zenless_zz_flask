from flask import Flask, render_template, session
from extensions import db
from routes.bangboo_stats import bp as bangboo_stats_bp
from routes.character_stats import bp as character_stats_bp
from routes.godfinger_stats import bp as godfinger_stats_bp
from routes.mewmew_stats import bp as mew_stats_bp
from routes.sage_stats import bp as sage_stats_bp
from routes.hdd_stats import bp as hdd_stats_bp
from seeds.seed_all import seed_all
from config.main_panel_stats import SECTIONS
from config.blueprints import BLUEPRINTS

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///zzz_db.sqlite'
    app.config['SECRET_KEY'] = '0JVJMsRPZunYykzxVfFIhQ'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    with app.app_context():
        db.create_all()
        seed_all()
        
    for bp in BLUEPRINTS:
        app.register_blueprint(bp)
    
    @app.route("/")
    def index():
        sections = {}
        for key, cfg in SECTIONS.items():
            service = cfg["service"]
            groups = service.get_all_groups()
            sections[key] = {
                "title": cfg["title"],
                "endpoint": cfg["endpoint"],
                "total": service.total_completed(),
                "list": [g[0] for g in groups],
                "summary": service.summary(),
            }
        return render_template("base.html",sections=sections)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
