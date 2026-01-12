from models.table_starhour import Starhour_stats
from .base_stats_service import BaseStatsService

class StarhourService(BaseStatsService):
    model = Starhour_stats
    id_field = "starhour_id"
    order_field = "starhour_id"
    status_field = "starhour_status"
    done_value = "Выполнено"
    undone_value = "Не выполнено"
    group_field = "starhour_section"
