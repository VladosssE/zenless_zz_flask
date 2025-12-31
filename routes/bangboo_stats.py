from flask import Blueprint, render_template, current_app, request, redirect, url_for, jsonify
from services.bangboo_stats_service import BangbooService
import os

bp = Blueprint("bangboo_stats", __name__, url_prefix="/bangboo_stats")


@bp.get("/")
def list_bangboo():
    bangboo = BangbooService.get_all()

    images_dir = os.path.join(
        current_app.root_path, "static", "images", "bangboo"
    )

    bangboo_img = [
        f for f in os.listdir(images_dir)
        if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
    ]

    return render_template(
        "bangboo_stats/index.html",
        bangboo=bangboo,
        bangboo_img=sorted(bangboo_img)
    )


@bp.post("/update")
def update_bangboo():
    data = request.get_json()
    
    BangbooService.update(
        bangboo_id=data["bangboo_id"],
        level=data.get("bangboo_level", 0),
        stars=data.get("bangboo_stars", 0),
    )
    return jsonify({"status": "ok"})
