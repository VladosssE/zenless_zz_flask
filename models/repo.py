from models.tables import db, Bangboo_stats

class BangbooStatsRepo:
    def __init__(self, db_instance=None):
        if db_instance:
            global db
            db = db_instance

    def all(self):
        return db.session.query(Bangboo_stats).all()

    def add(self, bangboo_name, bangboo_level, bangboo_stars, bangboo_class, image_url):
        new_bangboo = Bangboo_stats(
            bangboo_name = bangboo_name,
            bangboo_level = bangboo_level,
            bangboo_stars = bangboo_stars,
            bangboo_class = bangboo_class,
            image_url = image_url if image_url else None
            )
        db.session.add(new_bangboo)
        db.session.commit()
        return new_bangboo


class CharactersStatsRepo:
    def __init__(self, db_instance=None):
        if db_instance:
            global db
            db = db_instance

    def all(self):
        return db.session.query(Characters_stats).all()

    def add(self,
            character_name,
            character_type,
            character_class,
            character_level,
            character_mental_picture,
            character_skill_1,
            character_skill_2,
            character_skill_3,
            character_skill_4,
            character_skill_5,
            character_skill_strength,
            character_disk_1,
            character_disk_2,
            character_disk_3,
            character_disk_4,
            character_disk_5,
            character_disk_6,
            character_amplificator_unique,
            character_amplificator_level,
            character_amplificator_stars):
        
        new_character = Characters_stats(
            character_name = character_name,
            character_type = character_type,
            character_class = character_class,
            character_level = character_level,
            character_mental_picture = character_mental_picture,
            character_skill_1 = character_skill_1,
            character_skill_2 = character_skill_2,
            character_skill_3 = character_skill_3,
            character_skill_4 = character_skill_4,
            character_skill_5 = character_skill_5,
            character_skill_strength = character_skill_strength,
            character_disk_1 = character_disk_1,
            character_disk_2 = character_disk_2,
            character_disk_3 = character_disk_3,
            character_disk_4 = character_disk_4,
            character_disk_5 = character_disk_5,
            character_disk_6 = character_disk_6,
            character_amplificator_unique = character_amplificator_unique,
            character_amplificator_level = character_amplificator_level,
            character_amplificator_stars = character_amplificator_stars,
            image_url = image_url if image_url else None
            )
        db.session.add(new_character)
        db.session.commit()
        return new_character
