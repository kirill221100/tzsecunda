from typing import List

from pydantic import BaseModel, UUID4

#from src.schemas.organization import OrganizationBase


class BuildingBase(BaseModel):
    id: UUID4
    address: str
    latitude: float
    longitude: float

#class BuildingWithOrganizations(BuildingBase):
#    organizations: List[OrganizationBase]