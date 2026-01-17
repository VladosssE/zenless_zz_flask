from services.summer_stats_service import SummerService
from models.table_summer import Summer_stats
from .stats_func import create_stats_blueprint

bp = create_stats_blueprint(
    name="summer_stats",
    url_prefix="/summer_stats",
    service=SummerService,
    model=Summer_stats,
    template="summer_stats/index.html",
    filter_arg="section",
    get_all_filters=SummerService.get_all_groups,
    get_by_filter=SummerService.get_by_group,
    summary_func=SummerService.summary,
    id_field="summer_id",
    status_field="summer_status",
    status_done="Выполнено",
    status_not_done="Не выполнено"
)