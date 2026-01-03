from flask import Blueprint, render_template, current_app, request, redirect, url_for, jsonify
from services.mewmew_stats_service import MewmewService
from extensions import db
from models.tables import Mewmew_stats
import os

bp = Blueprint("mewmew_stats", __name__, url_prefix="/mewmew_stats")


@bp.get("/")
def list_mewmew():
    mewmew = MewmewService.get_all()
    current_street = request.args.get("street")
    streets = MewmewService.get_all_streets()
    summary = MewmewService.streets_summary()
    
    if streets:
        mewmew = MewmewService.get_by_street(current_street)
    else:
        mewmew = MewmewService.get_all()

    return render_template(
        "mewmew_stats/index.html",
        mewmew=mewmew,
        streets=[s[0] for s in streets],
        current_street=current_street,
        summary=summary
    )


@bp.route("/mewmew/complete_all", methods=["POST"])
def complete_all():
    MewmewService.complete_all()
    return redirect(request.referrer)


@bp.route("/update_mewmew", methods=["POST"])
def update_mewmew():
    data = request.get_json()
    if not data or "mew_id" not in data:
        return jsonify({"error": "Нет данных"}), 400

    mew_id = data["mew_id"]

    ach = Mewmew_stats.query.get(mew_id)
    if not ach:
        return jsonify({"error": "Не найдено"}), 404

    if ach.mew_status == "Выполнено":
        ach.mew_status = "Не выполнено"
    else:
        ach.mew_status = "Выполнено"

    db.session.commit()

    return jsonify({"status": ach.mew_status})
