from extensions import db
from models.tables import Character_stats

class CharacterService:

    @staticmethod
    def get_all():
        return Character_stats.query.order_by(Character_stats.character_id).all()

    @staticmethod
    def update(
        character_id,
        level=None,
        mental_picture=None,
        skills=None,
        skill_strength=None,
        disks=None,
        amplificator=None,
    ):
        character = Character_stats.query.get_or_404(character_id)

        if level is not None:
            character.character_level = int(level)

        if mental_picture is not None:
            character.character_mental_picture = int(mental_picture)

        if skills:
            for i, value in skills.items():
                if value is not None:
                    setattr(character, f"character_skill_{i}", int(value))

        if skill_strength:
            character.character_skill_strength = skill_strength

        if disks:
            for i, value in disks.items():
                if value is not None:
                    setattr(character, f"character_disk_{i}", int(value))

        if amplificator:
            character.character_amplificator_unique = amplificator["unique"]
            character.character_amplificator_level = int(amplificator["level"])
            character.character_amplificator_stars = int(amplificator["stars"])

        db.session.commit()
