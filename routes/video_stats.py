from services.video_stats_service import VideoService
from models.tables import Video_stats
from .stats_func import create_stats_blueprint

bp = create_stats_blueprint(
    name="video_stats",
    url_prefix="/video_stats",
    service=VideoService,
    model=Video_stats,
    template="video_stats/index.html",
    filter_arg="path",
    get_all_filters=VideoService.get_all_groups,
    get_by_filter=VideoService.get_by_group,
    summary_func=VideoService.summary,
    id_field="video_id",
    status_field="video_status",
    status_done="Пройдено",
    status_not_done="Не пройдено"
)
