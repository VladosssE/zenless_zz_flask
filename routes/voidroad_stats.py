from services.voidroad_stats_service import VoidroadService
from models.table_voidroad import Voidroad_stats
from .stats_func import create_stats_blueprint

bp = create_stats_blueprint(
    name="voidroad_stats",
    url_prefix="/voidroad_stats",
    service=VoidroadService,
    model=Voidroad_stats,
    template="voidroad_stats/index.html",
    filter_arg="section",
    get_all_filters=VoidroadService.get_all_groups,
    get_by_filter=VoidroadService.get_by_group,
    summary_func=VoidroadService.summary,
    id_field="voidroad_id",
    status_field="voidroad_status",
    status_done="Выполнено",
    status_not_done="Не выполнено"
)
