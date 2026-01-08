from flask import Flask, render_template, session
from extensions import db
from routes.bangboo_stats import bp as bangboo_stats_bp
from routes.character_stats import bp as character_stats_bp
from routes.godfinger_stats import bp as godfinger_stats_bp
from routes.mewmew_stats import bp as mew_stats_bp
from routes.sage_stats import bp as sage_stats_bp
from routes.hdd_stats import bp as hdd_stats_bp
from seeds.seed_all import seed_all
from services.godfinger_stats_service import GodfingerService
from services.mewmew_stats_service import MewmewService
from services.sage_stats_service import SageService
from services.hdd_stats_service import HddService
from routes.video_stats import bp as video_stats_bp
from services.video_stats_service import VideoService
from routes.friends_stats import bp as friends_stats_bp
from services.friends_stats_service import FriendsService
from routes.hollow_stats import bp as hollow_stats_bp
from services.hollow_stats_service import HollowService
from routes.hollow_withered_domain_stats import bp as hollow_withered_domain_stats_bp
from services.hollow_withered_domain_stats_service import HollowWDService

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///zzz_db.sqlite'
    app.config['SECRET_KEY'] = '0JVJMsRPZunYykzxVfFIhQ'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    with app.app_context():
        db.create_all()
        seed_all()
        
    app.register_blueprint(bangboo_stats_bp)
    app.register_blueprint(character_stats_bp)
    app.register_blueprint(godfinger_stats_bp)
    app.register_blueprint(mew_stats_bp)
    app.register_blueprint(sage_stats_bp)
    app.register_blueprint(hdd_stats_bp)
    app.register_blueprint(video_stats_bp)
    app.register_blueprint(friends_stats_bp)
    app.register_blueprint(hollow_stats_bp)
    app.register_blueprint(hollow_withered_domain_stats_bp)
    
    @app.route("/")
    def index():
        total_stats = GodfingerService.total_completed()
        games_list = GodfingerService.get_all_groups()
        games_summary = GodfingerService.summary()

        total_mewmew = MewmewService.total_completed()
        mewmew_list = MewmewService.get_all_groups()
        streets_summary = MewmewService.summary()

        total_sage = SageService.total_completed()
        sage_list = SageService.get_all_groups()
        sage_summary = SageService.summary()

        total_hdd = HddService.total_completed()
        hdd_list = HddService.get_all_groups()
        hdd_summary = HddService.summary()

        total_video = VideoService.total_completed()
        video_list = VideoService.get_all_groups()
        video_summary = VideoService.summary()

        total_friends = FriendsService.total_completed()
        friends_list = FriendsService.get_all_groups()
        friends_summary = FriendsService.summary()
        
        total_hollow = HollowService.total_completed()
        hollow_list = HollowService.get_all_groups()
        hollow_summary = HollowService.summary()

        total_hollow_wd = HollowWDService.total_completed()
        hollow_wd_list = HollowWDService.get_all_groups()
        hollow_wd_summary = HollowWDService.summary()
        
        return render_template(
            "base.html",
            total_stats=total_stats,
            games_list=[g[0] for g in games_list],
            summary=games_summary,
            total_mewmew=total_mewmew,
            mewmew_list=[l[0] for l in mewmew_list],
            mewmew_summary=streets_summary,
            total_sage=total_sage,
            sage_list=[l[0] for l in sage_list],
            sage_summary=sage_summary,
            total_hdd=total_hdd,
            hdd_list=[z[0] for z in hdd_list],
            hdd_summary=hdd_summary,
            total_video=total_video,
            video_list=[g[0] for g in video_list],
            video_summary=video_summary,
            total_friends=total_friends,
            friends_list=[g[0] for g in friends_list],
            friends_summary=friends_summary,
            total_hollow=total_hollow,
            hollow_list=[g[0] for g in hollow_list],
            hollow_summary=hollow_summary,
            total_hollow_wd=total_hollow_wd,
            hollow_wd_list=[g[0] for g in hollow_wd_list],
            hollow_wd_summary=hollow_wd_summary,
        )

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
