from models.tables import Friends_stats
from .base_stats_service import BaseStatsService

class FriendsService(BaseStatsService):
    model = Friends_stats
    id_field = Friends_stats.friends_id
    order_field = Friends_stats.friends_id

    status_field = "friends_status"
    done_value = "Максимальное доверие"
    undone_value = "Нет доверия"

    group_field = "friends_fraction"
