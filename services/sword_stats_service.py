from models.table_sword import Sword_stats
from .base_stats_service import BaseStatsService

class SwordService(BaseStatsService):
    model = Sword_stats
    id_field = "sword_id"
    order_field = "sword_id"
    status_field = "sword_status"
    done_value = "Выполнено"
    undone_value = "Не выполнено"
    group_field = "sword_section"