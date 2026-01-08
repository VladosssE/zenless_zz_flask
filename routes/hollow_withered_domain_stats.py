from services.hollow_withered_domain_stats_service import HollowWDService
from models.table_hollow_withered_domain import Hollow_withered_domain_stats
from .stats_func import create_stats_blueprint

bp = create_stats_blueprint(
    name="hollow_withered_domain_stats",
    url_prefix="/hollow_withered_domain_stats",
    service=HollowWDService,
    model=Hollow_withered_domain_stats,
    template="hollow_withered_domain_stats/index.html",
    filter_arg="section",
    get_all_filters=HollowWDService.get_all_groups,
    get_by_filter=HollowWDService.get_by_group,
    summary_func=HollowWDService.summary,
    id_field="hollow_wd_id",
    status_field="hollow_wd_status",
    status_done="Получено",
    status_not_done="Не получено"
)
