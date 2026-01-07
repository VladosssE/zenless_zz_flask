from models.table_video import Video_stats
from .base_stats_service import BaseStatsService

class VideoService(BaseStatsService):
    model = Video_stats
    id_field = Video_stats.video_id
    order_field = Video_stats.video_id

    status_field = "video_status"
    done_value = "Пройдено"
    undone_value = "Не пройдено"

    group_field = "video_path"
