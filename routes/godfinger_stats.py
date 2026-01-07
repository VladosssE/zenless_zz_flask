from services.godfinger_stats_service import GodfingerService
from models.table_godfinger import Godfinger_stats
from .stats_func import create_stats_blueprint

bp = create_stats_blueprint(
    name="godfinger_stats",
    url_prefix="/godfinger_stats",
    service=GodfingerService,
    model=Godfinger_stats,
    template="godfinger_stats/index.html",
    filter_arg="street",
    get_all_filters=GodfingerService.get_all_groups,
    get_by_filter=GodfingerService.get_by_group,
    summary_func=GodfingerService.summary,
    id_field="godfinger_id",
    status_field="godfinger_status",
    status_done="Выполнено",
    status_not_done="Не выполнено"
)
