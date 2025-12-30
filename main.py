from flask import Flask, render_template, session
from extensions import db
from models.tables import Bangboo_stats, Character_stats, Godfinger_stats
from routes.bangboo_stats import bp as bangboo_stats_bp
from routes.character_stats import bp as character_stats_bp
#from routes.godfinger_stats import bp as godfinger_stats_bp
from models.seed import seed_bangboo, seed_characters, seed_godfinger

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
        
    app.register_blueprint(bangboo_stats_bp)
    app.register_blueprint(character_stats_bp)
    #app.register_blueprint(godfinger_stats_bp)
    
    @app.route("/")
    def index():
        return render_template("base.html")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
