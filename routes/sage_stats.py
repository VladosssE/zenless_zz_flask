from services.sage_stats_service import SageService
from models.tables import Sage_stats
from .stats_func import create_stats_blueprint

bp = create_stats_blueprint(
    name="sage_stats",
    url_prefix="/sage_stats",
    service=SageService,
    model=Sage_stats,
    template="sage_stats/index.html",
    filter_arg="street",
    get_all_filters=SageService.get_all_groups,
    get_by_filter=SageService.get_by_group,
    summary_func=SageService.summary,
    id_field="sage_id",
    status_field="sage_status",
    status_done="Получено",
    status_not_done="Не получено"
)
