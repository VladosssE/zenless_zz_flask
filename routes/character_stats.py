from flask import Blueprint, render_template, current_app, request, redirect, url_for, jsonify
from services.character_stats_service import CharacterService
from extensions import db
import os

bp = Blueprint("characters_stats", __name__, url_prefix="/characters_stats")


@bp.get("/")
def list_characters():
    characters = CharacterService.get_all()
    cur_characters_type = request.args.get("c_type")
    characters_types = CharacterService.get_all_characters()
    
    images_dir = os.path.join(
        current_app.root_path, "static", "images", "characters"
    )
    
    characters_img = [
        f for f in os.listdir(images_dir)
        if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
    ]

    if characters_types:
        character_type = CharacterService.get_by_type(cur_characters_type)
    else:
        character_type = CharacterService.get_all()
    
    return render_template(
        "character_stats/index.html",
        characters=characters,
        characters_img=sorted(characters_img),
        characters_types=[c[0] for c in characters_types],
        cur_characters_type=cur_characters_type
    )


@bp.post("/update")
def update_characters():
    data = request.get_json()

    CharacterService.update(
        character_id=data["character_id"],

        level=data.get("character_level"),
        mental_picture=data.get("character_mental_picture"),

        skills={
            1: data.get("character_skill_1"),
            2: data.get("character_skill_2"),
            3: data.get("character_skill_3"),
            4: data.get("character_skill_4"),
            5: data.get("character_skill_5"),
        },

        skill_strength=data.get("character_skill_strength"),

        disks={
            1: data.get("character_disk_1"),
            2: data.get("character_disk_2"),
            3: data.get("character_disk_3"),
            4: data.get("character_disk_4"),
            5: data.get("character_disk_5"),
            6: data.get("character_disk_6"),
        },

        amplificator={
            "unique": data.get("character_amplificator_unique"),
            "level": data.get("character_amplificator_level"),
            "stars": data.get("character_amplificator_stars"),
        },
    )

    return jsonify({"status": "ok"})


