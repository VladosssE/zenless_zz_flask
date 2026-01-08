from models.table_hdd import Hdd_stats
from .base_stats_service import BaseStatsService

class HddService(BaseStatsService):
    model = Hdd_stats
    id_field = "hdd_id"
    order_field = "hdd_order"
    status_field = "hdd_status"
    done_value = "Всё собрано"
    undone_value = "Не пройдено"
    group_field = "hdd_chapter"
