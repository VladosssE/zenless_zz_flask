from models.table_hollow_withered_domain import Hollow_withered_domain_stats
from .base_stats_service import BaseStatsService

class HollowWDService(BaseStatsService):
    model = Hollow_withered_domain_stats
    id_field = "hollow_wd_id"
    order_field = "hollow_wd_id"
    status_field = "hollow_wd_status"
    done_value = "Получено"
    undone_value = "Не получено"
    group_field = "hollow_wd_section"
