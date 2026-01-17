from services.dream_stats_service import DreamService
from models.table_dream import Dream_stats
from .stats_func import create_stats_blueprint

bp = create_stats_blueprint(
    name="dream_stats",
    url_prefix="/dream_stats",
    service=DreamService,
    model=Dream_stats,
    template="dream_stats/index.html",
    filter_arg="section",
    get_all_filters=DreamService.get_all_groups,
    get_by_filter=DreamService.get_by_group,
    summary_func=DreamService.summary,
    id_field="dream_id",
    status_field="dream_status",
    status_done="Выполнено",
    status_not_done="Не выполнено"
)