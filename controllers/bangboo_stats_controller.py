from flask import Blueprint, render_template, current_app, request, redirect, url_for
from models.tables import db, Bangboo_stats
from models.repo import BangbooStatsRepo
from sqlalchemy import text
import os

bp = Blueprint("bangboo_stats", __name__, url_prefix="/bangboo_stats")
repo = BangbooStatsRepo()


@bp.get("/")
def list_bangboo():
    cursor = db.session.execute(text("SELECT bangboo_id, bangboo_name, bangboo_level, bangboo_stars, bangboo_class, bangboo_image_url FROM bangboo_stats_zzz"))
    bangboo = cursor.fetchall()
    images_dir = os.path.join(current_app.root_path, "static", "images", "bangboo")
    bangboo_img = [
        f for f in os.listdir(images_dir)
        if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
        and f.lower() not in ("placeholder.jpg", "no_film.jpg")
    ]
    return render_template("list_bangboo_stats.html", bangboo=bangboo, bangboo_img=sorted(bangboo_img))


def update_bangboo(id_get, level_input, stars_input):
    db.session.execute(text("UPDATE bangboo_stats_zzz SET bangboo_level = :lvl, bangboo_stars = :strs WHERE bangboo_id = :id"),
        {
            "lvl": level_input,
            "strs": stars_input,
            "id": id_get
        }
    )
    db.session.commit()


@bp.route('/update', methods=["POST"])
def get_update_bangboo():
    id_get = request.form.get("bangboo_id")
    level_input = request.form.get("bangboo_level")
    stars_input = request.form.get("bangboo_stars")
    update_bangboo(id_get, level_input, stars_input)
    return redirect(url_for("bangboo_stats.list_bangboo"))



