from src.schemas import BuildingBase, OrganizationBase
from typing import List

class BuildingWithOrganizations(BuildingBase):
    organizations: List[OrganizationBase]