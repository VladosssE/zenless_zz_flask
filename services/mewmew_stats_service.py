from models.table_mewmew import Mewmew_stats
from .base_stats_service import BaseStatsService

class MewmewService(BaseStatsService):
    model = Mewmew_stats
    id_field = "mew_id"
    order_field = "mew_id"
    status_field = "mew_status"
    done_value = "Выполнено"
    undone_value = "Не выполнено"
    group_field = "mew_street"
