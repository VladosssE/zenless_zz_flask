from services.friends_stats_service import FriendsService
from models.table_friends import Friends_stats
from .stats_func import create_stats_blueprint

bp = create_stats_blueprint(
    name="friends_stats",
    url_prefix="/friends_stats",
    service=FriendsService,
    model=Friends_stats,
    template="friends_stats/index.html",
    filter_arg="fraction",
    get_all_filters=FriendsService.get_all_groups,
    get_by_filter=FriendsService.get_by_group,
    summary_func=FriendsService.summary,
    id_field="friends_id",
    status_field="friends_status",
    status_done="Максимальное доверие",
    status_not_done="Нет доверия"
)
