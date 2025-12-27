from flask import Blueprint, render_template, current_app, request, redirect, url_for
from models.tables import db, Characters_stats
from models.repo import CharactersStatsRepo
from sqlalchemy import text
import os

bp = Blueprint("characters_stats", __name__, url_prefix="/characters_stats")
repo = CharactersStatsRepo()


@bp.get("/")
def list_characters():
    cursor = db.session.execute(text("""
                                        SELECT
                                                character_id, character_name, character_type,
                                                character_class, character_level, character_mental_picture,
                                                character_skill_1, character_skill_2, character_skill_3,
                                                character_skill_4, character_skill_5, character_skill_strength,
                                                character_disk_1, character_disk_2, character_disk_3,
                                                character_disk_4, character_disk_5, character_disk_6,
                                                character_amplificator_unique, character_amplificator_level, character_amplificator_stars, character_image_url
                                        FROM
                                                characters_stats_zzz
                                    """))
    characters = cursor.fetchall()
    images_dir = os.path.join(current_app.root_path, "static", "images", "characters")
    characters_img = [
        f for f in os.listdir(images_dir)
        if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
        and f.lower() not in ("placeholder.jpg", "no_film.jpg")
    ]
    return render_template("list_characters_stats.html", characters=characters, characters_img=sorted(characters_img))


def update_characters(id_get, level_input, mental_input, skill_1_input, skill_2_input, skill_3_input, skill_4_input, skill_5_input,
                      skill_strength_input, disk_1_input, disk_2_input, disk_3_input, disk_4_input, disk_5_input,
                      disk_6_input, amp_uniq_input, amp_level_input, amp_stars_input):
    db.session.execute(text("""
                                UPDATE characters_stats_zzz SET
                                character_level= :lvl,
                                character_mental_picture= :cmp,
                                character_skill_1= :cs1,
                                character_skill_2= :cs2,
                                character_skill_3= :cs3,
                                character_skill_4= :cs4,
                                character_skill_5= :cs5,
                                character_skill_strength= :css,
                                character_disk_1= :cd1,
                                character_disk_2= :cd2,
                                character_disk_3= :cd3,
                                character_disk_4= :cd4,
                                character_disk_5= :cd5,
                                character_disk_6= :cd6,
                                character_amplificator_unique= :cau,
                                character_amplificator_level= :cal,
                                character_amplificator_stars= :cas
                                WHERE character_id= :cid
                            """),
        {
            "lvl": level_input,
            "cmp": mental_input,
            "cs1": skill_1_input,
            "cs2": skill_2_input,
            "cs3": skill_3_input,
            "cs4": skill_4_input,
            "cs5": skill_5_input,
            "css": skill_strength_input,
            "cd1": disk_1_input,
            "cd2": disk_2_input,
            "cd3": disk_3_input,
            "cd4": disk_4_input,
            "cd5": disk_5_input,
            "cd6": disk_6_input,
            "cau": amp_uniq_input,
            "cal": amp_level_input,
            "cas": amp_stars_input,
            "cid": id_get
        }
    )
    db.session.commit()


@bp.route('/update', methods=["POST"])
def get_update_characters():
    id_get = request.form.get("character_id")
    level_input = request.form.get("character_level")
    mental_input = request.form.get("character_mental_picture")
    skill_1_input = request.form.get("character_skill_1")
    skill_2_input = request.form.get("character_skill_2")
    skill_3_input = request.form.get("character_skill_3")
    skill_4_input = request.form.get("character_skill_4")
    skill_5_input = request.form.get("character_skill_5")
    skill_strength_input = request.form.get("character_skill_strength")
    disk_1_input = request.form.get("character_disk_1")
    disk_2_input = request.form.get("character_disk_2")
    disk_3_input = request.form.get("character_disk_3")
    disk_4_input = request.form.get("character_disk_4")
    disk_5_input = request.form.get("character_disk_5")
    disk_6_input = request.form.get("character_disk_6")
    amp_uniq_input = request.form.get("character_amplificator_unique")
    amp_level_input = request.form.get("character_amplificator_level")
    amp_stars_input = request.form.get("character_amplificator_stars")
    
    update_characters(id_get, level_input, mental_input, skill_1_input, skill_2_input, skill_3_input, skill_4_input, skill_5_input,
                   skill_strength_input, disk_1_input, disk_2_input, disk_3_input, disk_4_input, disk_5_input,
                   disk_6_input, amp_uniq_input, amp_level_input, amp_stars_input)
    return redirect(url_for("characters_stats.list_characters"))



