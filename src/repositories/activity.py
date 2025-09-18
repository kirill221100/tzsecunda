from .base import BaseRepository
from src.models.activity import Activity


class ActivityRepository(BaseRepository[Activity]):
    table = Activity
