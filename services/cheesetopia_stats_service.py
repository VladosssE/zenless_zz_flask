from models.table_cheesetopia import Cheesetopia_stats
from .base_stats_service import BaseStatsService

class CheesetopiaService(BaseStatsService):
    model = Cheesetopia_stats
    id_field = "cheesetopia_id"
    order_field = "cheesetopia_id"
    status_field = "cheesetopia_status"
    done_value = "Выполнено"
    undone_value = "Не выполнено"
    group_field = "cheesetopia_section"
