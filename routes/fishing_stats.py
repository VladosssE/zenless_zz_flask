from services.fishing_stats_service import FishingService
from models.table_fishing import Fishing_stats
from .stats_func import create_stats_blueprint

bp = create_stats_blueprint(
    name="fishing_stats",
    url_prefix="/fishing_stats",
    service=FishingService,
    model=Fishing_stats,
    template="fishing_stats/index.html",
    filter_arg="section",
    get_all_filters=FishingService.get_all_groups,
    get_by_filter=FishingService.get_by_group,
    summary_func=FishingService.summary,
    id_field="fishing_id",
    status_field="fishing_status",
    status_done="Выполнено",
    status_not_done="Не выполнено"
)
