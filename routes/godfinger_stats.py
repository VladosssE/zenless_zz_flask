from flask import Blueprint, render_template, current_app, request, redirect, url_for, jsonify
from services.godfinger_stats_service import GodfingerService
from extensions import db
from models.tables import Godfinger_stats
import os

bp = Blueprint("godfinger_stats", __name__, url_prefix="/godfinger_stats")


@bp.get("/")
def list_godfinger():
    godfinger = GodfingerService.get_all()
    current_game = request.args.get("game")
    games = GodfingerService.get_all_games()
    summary = GodfingerService.achievements_summary()
    
    images_dir = os.path.join(
        current_app.root_path, "static", "icons", "godfinger"
    )

    godfinger_img = [
        f for f in os.listdir(images_dir)
        if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
    ]

    if games:
        godfinger = GodfingerService.get_by_game(current_game)
    else:
        godfinger = GodfingerService.get_all()

    return render_template(
        "godfinger_stats/index.html",
        godfinger=godfinger,
        godfinger_img=sorted(godfinger_img),
        games=[g[0] for g in games],
        current_game=current_game,
        summary=summary
    )


@bp.route("/update_godfinger", methods=["POST"])
def update_godfinger():
    data = request.get_json()
    if not data or "godfinger_id" not in data:
        return jsonify({"error": "Нет данных"}), 400

    godfinger_id = data["godfinger_id"]

    ach = Godfinger_stats.query.get(godfinger_id)
    if not ach:
        return jsonify({"error": "Достижение не найдено"}), 404

    if ach.godfinger_status == "Выполнено":
        ach.godfinger_status = "Не выполнено"
    else:
        ach.godfinger_status = "Выполнено"

    db.session.commit()

    return jsonify({"status": ach.godfinger_status})
