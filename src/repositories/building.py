from .base import BaseRepository
from src.models.building import Building

class BuildingRepository(BaseRepository[Building]):
    table = Building
