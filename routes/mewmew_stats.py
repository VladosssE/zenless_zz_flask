from services.mewmew_stats_service import MewmewService
from models.table_mewmew import Mewmew_stats
from .stats_func import create_stats_blueprint

bp = create_stats_blueprint(
    name="mewmew_stats",
    url_prefix="/mewmew_stats",
    service=MewmewService,
    model=Mewmew_stats,
    template="mewmew_stats/index.html",
    filter_arg="street",
    get_all_filters=MewmewService.get_all_groups,
    get_by_filter=MewmewService.get_by_group,
    summary_func=MewmewService.summary,
    id_field="mew_id",
    status_field="mew_status",
    status_done="Выполнено",
    status_not_done="Не выполнено"
)
