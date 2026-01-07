from models.table_hdd import Hdd_stats
from .base_stats_service import BaseStatsService

class HddService(BaseStatsService):
    model = Hdd_stats
    id_field = Hdd_stats.hdd_id
    order_field = Hdd_stats.hdd_id

    status_field = "hdd_status"
    done_value = "Всё собрано"
    undone_value = "Не пройдено"

    group_field = "hdd_chapter"
