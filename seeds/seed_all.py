from .seed_bangboo import seed_bangboo
from .seed_characters import seed_characters
from .seed_godfinger import seed_godfinger
from .seed_mewmew import seed_mewmew
from .seed_sage import seed_sage
from .seed_hdd import seed_hdd
from .seed_video import seed_video
from .seed_friends import seed_friends
from .seed_hollow import seed_hollow
from .seed_hollow_withered_domain import seed_hollow_withered_domain
from .seed_events import seed_events
from .seed_hollow_lost_void import seed_hollow_lost_void
from .seed_cheesetopia import seed_cheesetopia
from .seed_starhour import seed_starhour
from .seed_voidroad import seed_voidroad
from .seed_fishing import seed_fishing
from .seed_flowers import seed_flowers
from .seed_gravity import seed_gravity
from .seed_sword import seed_sword
from .seed_summer import seed_summer
from .seed_dream import seed_dream

def seed_all():
    print(f"[ 000 ][ {'Прямо сейчас добавляются и проверяются данные в таблицах':<82} ]")
    seed_bangboo()
    seed_characters()
    seed_godfinger()
    seed_mewmew()
    seed_sage()
    seed_hdd()
    seed_video()
    seed_friends()
    seed_hollow()
    seed_hollow_withered_domain()
    seed_events()
    seed_hollow_lost_void()
    seed_cheesetopia()
    seed_starhour()
    seed_voidroad()
    seed_fishing()
    seed_flowers()
    seed_gravity()
    seed_sword() 
    seed_summer() 
    seed_dream()
