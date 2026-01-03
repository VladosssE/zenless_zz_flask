from flask import Blueprint, render_template, current_app, request, redirect, url_for, jsonify
from services.sage_stats_service import SageService
from extensions import db
from models.tables import Sage_stats
import os

bp = Blueprint("sage_stats", __name__, url_prefix="/sage_stats")


@bp.get("/")
def list_sage():
    sage = SageService.get_all()
    current_street = request.args.get("street")
    streets = SageService.get_all_streets()
    summary = SageService.streets_summary()
    
    if streets:
        sage = SageService.get_by_street(current_street)
    else:
        sage = SageService.get_all()

    return render_template(
        "sage_stats/index.html",
        sage=sage,
        streets=[s[0] for s in streets],
        current_street=current_street,
        summary=summary
    )


@bp.route("/sage/complete_day/<day>", methods=["POST"])
def complete_day(day):
    SageService.complete_day(day)
    return redirect(request.referrer)


@bp.route("/sage/complete_all", methods=["POST"])
def complete_all():
    SageService.complete_all()
    return redirect(request.referrer)


@bp.route("/update_sage", methods=["POST"])
def update_sage():
    data = request.get_json()
    if not data or "sage_id" not in data:
        return jsonify({"error": "Нет данных"}), 400

    sage_id = data["sage_id"]

    ach = Sage_stats.query.get(sage_id)
    if not ach:
        return jsonify({"error": "Не найдено"}), 404

    if ach.sage_status == "Получено":
        ach.sage_status = "Не получено"
    else:
        ach.sage_status = "Получено"

    db.session.commit()

    return jsonify({"status": ach.sage_status})
