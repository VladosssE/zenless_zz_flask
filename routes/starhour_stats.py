from services.starhour_stats_service import StarhourService
from models.table_starhour import Starhour_stats
from .stats_func import create_stats_blueprint

bp = create_stats_blueprint(
    name="starhour_stats",
    url_prefix="/starhour_stats",
    service=StarhourService,
    model=Starhour_stats,
    template="starhour_stats/index.html",
    filter_arg="section",
    get_all_filters=StarhourService.get_all_groups,
    get_by_filter=StarhourService.get_by_group,
    summary_func=StarhourService.summary,
    id_field="starhour_id",
    status_field="starhour_status",
    status_done="Выполнено",
    status_not_done="Не выполнено"
)
