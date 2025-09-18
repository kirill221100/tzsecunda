from .base import BaseRepository
from src.models.organization import Organization

class OrganisationRepository(BaseRepository[Organization]):
    table = Organization
