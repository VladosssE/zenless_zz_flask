from models.tables import Sage_stats
from .base_stats_service import BaseStatsService

class SageService(BaseStatsService):
    model = Sage_stats
    id_field = Sage_stats.sage_id
    order_field = Sage_stats.sage_id

    status_field = "sage_status"
    done_value = "Получено"
    undone_value = "Не получено"

    group_field = "sage_street"
