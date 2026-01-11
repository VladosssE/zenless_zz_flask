from services.hollow_lost_void_stats_service import Hollow_lvService
from models.table_hollow_lost_void import Hollow_lost_void_stats
from .stats_func import create_stats_blueprint

bp = create_stats_blueprint(
    name="hollow_lost_void_stats",
    url_prefix="/hollow_lost_void_stats",
    service=Hollow_lvService,
    model=Hollow_lost_void_stats,
    template="hollow_lost_void_stats/index.html",
    filter_arg="hollow_lv_section",
    get_all_filters=Hollow_lvService.get_all_groups,
    get_by_filter=Hollow_lvService.get_by_group,
    summary_func=Hollow_lvService.summary,
    id_field="hollow_lv_id",
    status_field="hollow_lv_status",
    status_done="Получено",
    status_not_done="Не получено"
)
