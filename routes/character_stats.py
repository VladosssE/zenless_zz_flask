from flask import Blueprint, render_template, current_app, request, redirect, url_for
from services.character_stats_service import CharacterService
import os

bp = Blueprint("characters_stats", __name__, url_prefix="/characters_stats")


@bp.get("/")
def list_characters():
    characters = CharacterService.get_all()
    
    images_dir = os.path.join(
        current_app.root_path, "static", "images", "characters"
    )
    
    characters_img = [
        f for f in os.listdir(images_dir)
        if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
    ]
    
    return render_template(
        "character_stats/index.html",
        characters=characters,
        characters_img=sorted(characters_img)
    )


@bp.post("/update")
def update_characters():
    form = request.form
    
    CharacterService.update(
        character_id=form["character_id"],
        level=form.get("character_level"),
        mental_picture=form.get("character_mental_picture"),
        skills={
            1: form.get("character_skill_1"),
            2: form.get("character_skill_2"),
            3: form.get("character_skill_3"),
            4: form.get("character_skill_4"),
            5: form.get("character_skill_5"),
        },
        skill_strength=form.get("character_skill_strength"),
        disks={
            1: form.get("character_disk_1"),
            2: form.get("character_disk_2"),
            3: form.get("character_disk_3"),
            4: form.get("character_disk_4"),
            5: form.get("character_disk_5"),
        },
        amplificator={
            "unique": form.get("character_amplificator_unique"),
            "level": form.get("character_amplificator_level"),
            "stars": form.get("character_amplificator_stars"),
        }
    )

    return redirect(url_for("characters_stats.list_characters"))
