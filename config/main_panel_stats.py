from services.godfinger_stats_service import GodfingerService
from services.mewmew_stats_service import MewmewService
from services.sage_stats_service import SageService
from services.hdd_stats_service import HddService
from services.video_stats_service import VideoService
from services.friends_stats_service import FriendsService
from services.hollow_withered_domain_stats_service import HollowWDService
from services.events_stats_service import EventsService
from services.hollow_lost_void_stats_service import Hollow_lvService
from services.cheesetopia_stats_service import CheesetopiaService
from services.starhour_stats_service import StarhourService
from services.voidroad_stats_service import VoidroadService

SECTIONS = {
    "events": {
        "title": "События",
        "service": EventsService,
        "endpoint": "events_stats.list_data",
    },
    "friends": {
        "title": "Партнёры",
        "service": FriendsService,
        "endpoint": "friends_stats.list_data",
    },
    "godfinger": {
        "title": "Годфингер",
        "service": GodfingerService,
        "endpoint": "godfinger_stats.list_data",
    },
    "mewmew": {
        "title": "Инспектор Мяучело",
        "service": MewmewService,
        "endpoint": "mewmew_stats.list_data",
    },
    "sage": {
        "title": "Мудрец в бочке",
        "service": SageService,
        "endpoint": "sage_stats.list_data",
    },
    "hdd": {
        "title": "H.D.D.",
        "service": HddService,
        "endpoint": "hdd_stats.list_data",
    },
    "video": {
        "title": "Видеоархив",
        "service": VideoService,
        "endpoint": "video_stats.list_data",
    },
    "hollow_withered_domain": {
        "title": "Каверна: Город увядания",
        "service": HollowWDService,
        "endpoint": "hollow_withered_domain_stats.list_data",
    },
    "hollow_lost_void": {
        "title": "Каверна: Затерянная бездна",
        "service": Hollow_lvService,
        "endpoint": "hollow_lost_void_stats.list_data",
    },
    "cheesetopia": {
        "title": "Сырополис",
        "service": CheesetopiaService,
        "endpoint": "cheesetopia_stats.list_data",
    },
    "starhour": {
        "title": "Звёздный час",
        "service": StarhourService,
        "endpoint": "starhour_stats.list_data",
    },
    "voidroad": {
        "title": "Дорога в пустоту",
        "service": VoidroadService,
        "endpoint": "voidroad_stats.list_data",
    },
}
