from models.table_sage import Sage_stats
from .base_stats_service import BaseStatsService

class SageService(BaseStatsService):
    model = Sage_stats
    id_field = "sage_id"
    order_field = "sage_id"
    status_field = "sage_status"
    done_value = "Получено"
    undone_value = "Не получено"
    group_field = "sage_street"
