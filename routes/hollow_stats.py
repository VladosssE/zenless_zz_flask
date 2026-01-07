from services.hollow_stats_service import HollowService
from models.table_hollow import Hollow_stats
from .stats_func import create_stats_blueprint

bp = create_stats_blueprint(
    name="hollow_stats",
    url_prefix="/hollow_stats",
    service=HollowService,
    model=Hollow_stats,
    template="hollow_stats/index.html",
    filter_arg="name",
    get_all_filters=HollowService.get_all_groups,
    get_by_filter=HollowService.get_by_group,
    summary_func=HollowService.summary,
    id_field="hollow_id",
    status_field="hollow_status",
    status_done="Пройдено",
    status_not_done="Не пройдено"
)
