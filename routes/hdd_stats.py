from flask import Blueprint, render_template, current_app, request, redirect, url_for, jsonify
from services.hdd_stats_service import HddService
from extensions import db
from models.tables import Hdd_stats
import os

bp = Blueprint("hdd_stats", __name__, url_prefix="/hdd_stats")


@bp.get("/")
def list_hdd():
    listing = HddService.get_all()
    current = request.args.get("chapter")
    getall = HddService.get_all_chapters()
    summary = HddService.chapters_summary()
    
    if getall:
        listing = HddService.get_by_chapter(current)
    else:
        listing = HddService.get_all()

    return render_template(
        "hdd_stats/index.html",
        listing=listing,
        getall=[z[0] for z in getall],
        current=current,
        summary=summary
    )


@bp.route("/hdd/complete_all", methods=["POST"])
def complete_all():
    HddService.complete_all()
    return redirect(request.referrer)


@bp.route("/update_hdd", methods=["POST"])
def update_hdd():
    data = request.get_json()
    if not data or "hdd_id" not in data:
        return jsonify({"error": "Нет данных"}), 400

    hdd_id = data["hdd_id"]

    ach = Hdd_stats.query.get(hdd_id)
    if not ach:
        return jsonify({"error": "Не найдено"}), 404

    if ach.hdd_status == "Всё собрано":
        ach.hdd_status = "Не пройдено"
    else:
        ach.hdd_status = "Всё собрано"

    db.session.commit()

    return jsonify({"status": ach.hdd_status})
