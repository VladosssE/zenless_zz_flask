from models.table_godfinger import Godfinger_stats
from .base_stats_service import BaseStatsService

class GodfingerService(BaseStatsService):
    model = Godfinger_stats
    id_field = "godfinger_id"
    order_field = "godfinger_id"
    status_field = "godfinger_status"
    done_value = "Выполнено"
    undone_value = "Не выполнено"
    group_field = "godfinger_game"
