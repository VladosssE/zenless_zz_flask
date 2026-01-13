from models.table_flowers import Flowers_stats
from .base_stats_service import BaseStatsService

class FlowersService(BaseStatsService):
    model = Flowers_stats
    id_field = "flowers_id"
    order_field = "flowers_id"
    status_field = "flowers_status"
    done_value = "Выполнено"
    undone_value = "Не выполнено"
    group_field = "flowers_section"
