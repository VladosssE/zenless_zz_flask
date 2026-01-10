from services.events_stats_service import EventsService
from models.table_events import Events_stats
from .stats_func import create_stats_blueprint

bp = create_stats_blueprint(
    name="events_stats",
    url_prefix="/events_stats",
    service=EventsService,
    model=Events_stats,
    template="events_stats/index.html",
    filter_arg="version",
    get_all_filters=EventsService.get_all_groups,
    get_by_filter=EventsService.get_by_group,
    summary_func=EventsService.summary,
    id_field="events_id",
    status_field="events_status",
    status_done="Завершено",
    status_not_done="Не пройден"
)
