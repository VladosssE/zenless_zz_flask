from services.flowers_stats_service import FlowersService
from models.table_flowers import Flowers_stats
from .stats_func import create_stats_blueprint

bp = create_stats_blueprint(
    name="flowers_stats",
    url_prefix="/flowers_stats",
    service=FlowersService,
    model=Flowers_stats,
    template="flowers_stats/index.html",
    filter_arg="section",
    get_all_filters=FlowersService.get_all_groups,
    get_by_filter=FlowersService.get_by_group,
    summary_func=FlowersService.summary,
    id_field="flowers_id",
    status_field="flowers_status",
    status_done="Выполнено",
    status_not_done="Не выполнено"
)
