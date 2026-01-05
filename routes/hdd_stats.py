from services.hdd_stats_service import HddService
from models.tables import Hdd_stats
from .stats_func import create_stats_blueprint

bp = create_stats_blueprint(
    name="hdd_stats",
    url_prefix="/hdd_stats",
    service=HddService,
    model=Hdd_stats,
    template="hdd_stats/index.html",
    filter_arg="chapter",
    get_all_filters=HddService.get_all_groups,
    get_by_filter=HddService.get_by_group,
    summary_func=HddService.summary,
    id_field="hdd_id",
    status_field="hdd_status",
    status_done="Всё собрано",
    status_not_done="Не пройдено"
)
