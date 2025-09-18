from typing import Annotated, List, Optional
from pydantic import BaseModel, StringConstraints, UUID4
from src.schemas.activity import ActivityBase
from src.schemas.building import BuildingBase


class OrganizationBase(BaseModel):
    id: UUID4
    name: str
    phone_numbers: List[str]
    building_id: UUID4

class OrganizationWithActivities(OrganizationBase):
    activities: List[ActivityBase]

class OrganizationWithActivitiesAndBuilding(OrganizationWithActivities):
    building: BuildingBase
