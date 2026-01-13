from services.gravity_stats_service import GravityService
from models.table_gravity import Gravity_stats
from .stats_func import create_stats_blueprint

bp = create_stats_blueprint(
    name="gravity_stats",
    url_prefix="/gravity_stats",
    service=GravityService,
    model=Gravity_stats,
    template="gravity_stats/index.html",
    filter_arg="section",
    get_all_filters=GravityService.get_all_groups,
    get_by_filter=GravityService.get_by_group,
    summary_func=GravityService.summary,
    id_field="gravity_id",
    status_field="gravity_status",
    status_done="Выполнено",
    status_not_done="Не выполнено"
)
