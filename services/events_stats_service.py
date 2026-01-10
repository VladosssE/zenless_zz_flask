from models.table_events import Events_stats
from .base_stats_service import BaseStatsService

class EventsService(BaseStatsService):
    model = Events_stats
    id_field = "events_id"
    order_field = "events_id"
    status_field = "events_status"
    done_value = "Завершено"
    undone_value = "Не пройден"
    group_field = "events_version"
