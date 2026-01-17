from services.sword_stats_service import SwordService
from models.table_sword import Sword_stats
from .stats_func import create_stats_blueprint

bp = create_stats_blueprint(
    name="sword_stats",
    url_prefix="/sword_stats",
    service=SwordService,
    model=Sword_stats,
    template="sword_stats/index.html",
    filter_arg="section",
    get_all_filters=SwordService.get_all_groups,
    get_by_filter=SwordService.get_by_group,
    summary_func=SwordService.summary,
    id_field="sword_id",
    status_field="sword_status",
    status_done="Выполнено",
    status_not_done="Не выполнено"
)