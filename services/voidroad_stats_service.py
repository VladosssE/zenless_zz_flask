from models.table_voidroad import Voidroad_stats
from .base_stats_service import BaseStatsService

class VoidroadService(BaseStatsService):
    model = Voidroad_stats
    id_field = "voidroad_id"
    order_field = "voidroad_id"
    status_field = "voidroad_status"
    done_value = "Выполнено"
    undone_value = "Не выполнено"
    group_field = "voidroad_section"
