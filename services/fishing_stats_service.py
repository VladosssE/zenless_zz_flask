from models.table_fishing import Fishing_stats
from .base_stats_service import BaseStatsService

class FishingService(BaseStatsService):
    model = Fishing_stats
    id_field = "fishing_id"
    order_field = "fishing_id"
    status_field = "fishing_status"
    done_value = "Выполнено"
    undone_value = "Не выполнено"
    group_field = "fishing_section"
