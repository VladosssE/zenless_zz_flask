from models.table_dream import Dream_stats
from .base_stats_service import BaseStatsService

class DreamService(BaseStatsService):
    model = Dream_stats
    id_field = "dream_id"
    order_field = "dream_id"
    status_field = "dream_status"
    done_value = "Выполнено"
    undone_value = "Не выполнено"
    group_field = "dream_section"