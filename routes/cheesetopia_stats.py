from services.cheesetopia_stats_service import CheesetopiaService
from models.table_cheesetopia import Cheesetopia_stats
from .stats_func import create_stats_blueprint

bp = create_stats_blueprint(
    name="cheesetopia_stats",
    url_prefix="/cheesetopia_stats",
    service=CheesetopiaService,
    model=Cheesetopia_stats,
    template="cheesetopia_stats/index.html",
    filter_arg="section",
    get_all_filters=CheesetopiaService.get_all_groups,
    get_by_filter=CheesetopiaService.get_by_group,
    summary_func=CheesetopiaService.summary,
    id_field="cheesetopia_id",
    status_field="cheesetopia_status",
    status_done="Выполнено",
    status_not_done="Не выполнено"
)
