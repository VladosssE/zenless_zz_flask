from models.table_hollow import Hollow_stats
from .base_stats_service import BaseStatsService

class HollowService(BaseStatsService):
    model = Hollow_stats
    id_field = "hollow_id"
    order_field = "hollow_id"
    status_field = "hollow_status"
    done_value = "Пройдено"
    undone_value = "Не пройдено"
    group_field = "hollow_name"
