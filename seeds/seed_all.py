from .seed_bangboo import seed_bangboo
from .seed_characters import seed_characters
from .seed_godfinger import seed_godfinger
from .seed_mewmew import seed_mewmew
from .seed_sage import seed_sage
from .seed_hdd import seed_hdd
from .seed_video import seed_video
from .seed_friends import seed_friends
from .seed_hollow import seed_hollow

def seed_all():
    print(f"[ 000 ][ {'Прямо сейчас добавляются и проверяются данные в таблицах':<72} ]")
    seed_bangboo()
    seed_characters()
    seed_godfinger()
    seed_mewmew()
    seed_sage()
    seed_hdd()
    seed_video()
    seed_friends()
    seed_hollow()
