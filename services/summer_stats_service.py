from models.table_summer import Summer_stats
from .base_stats_service import BaseStatsService

class SummerService(BaseStatsService):
    model = Summer_stats
    id_field = "summer_id"
    order_field = "summer_id"
    status_field = "summer_status"
    done_value = "Выполнено"
    undone_value = "Не выполнено"
    group_field = "summer_section"