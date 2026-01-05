from models.tables import Mewmew_stats
from .base_stats_service import BaseStatsService

class MewmewService(BaseStatsService):
    model = Mewmew_stats
    id_field = Mewmew_stats.mew_id
    order_field = Mewmew_stats.mew_id

    status_field = "mew_status"
    done_value = "Выполнено"
    undone_value = "Не выполнено"

    group_field = "mew_street"
