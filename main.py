from flask import Flask, render_template, session
from models.tables import db, Bangboo_stats, Characters_stats
from controllers.bangboo_stats_controller import bp as bangboo_stats_bp
from controllers.characters_stats_controller import bp as characters_stats_bp
from models.seed import seed_bangboo, seed_characters

def create_app():
    app = Flask(__name__, template_folder="views", static_folder="static")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///zzz_db.sqlite'
    app.config['SECRET_KEY'] = '0JVJMsRPZunYykzxVfFIhQ'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    with app.app_context():
        db.create_all()
        seed_bangboo()
        seed_characters()
        
    app.register_blueprint(bangboo_stats_bp)
    app.register_blueprint(characters_stats_bp)
    
    @app.route("/")
    def index():
        main = db.session.query(Bangboo_stats).all()
        return render_template("index.html", main=main)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
