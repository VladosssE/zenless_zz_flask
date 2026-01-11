from models.table_hollow_lost_void import Hollow_lost_void_stats
from .base_stats_service import BaseStatsService

class Hollow_lvService(BaseStatsService):
    model = Hollow_lost_void_stats
    id_field = "hollow_lv_id"
    order_field = "hollow_lv_id"
    status_field = "hollow_lv_status"
    done_value = "Получено"
    undone_value = "Не получено"
    group_field = "hollow_lv_section"
