from models.table_gravity import Gravity_stats
from .base_stats_service import BaseStatsService

class GravityService(BaseStatsService):
    model = Gravity_stats
    id_field = "gravity_id"
    order_field = "gravity_id"
    status_field = "gravity_status"
    done_value = "Выполнено"
    undone_value = "Не выполнено"
    group_field = "gravity_section"
