from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import UUID4
from sqlalchemy.orm import load_only, selectinload

from src import database as db
from src.models import Organization, Activity
from src.repositories.building import BuildingRepository


class BuildingService:
    def __init__(self, session: AsyncSession = Depends(db.get_async_session)):
        self.session = session
        self.building_repo = BuildingRepository(session=session)

    async def get_with_organizations(self, building_id):
        return await self.building_repo.get_one_by_filter_with_options(
            [BuildingRepository.table.id == building_id],
            [
                load_only(BuildingRepository.table.id),
                selectinload(
                    BuildingRepository.table.organizations
                ).selectinload(
                    Organization.activities
                ).load_only(Activity.id, Activity.name)
            ]
        )

    async def get_all_within_radius(self, latitude: float, longitude: float, radius_meters: int):
        delta_deg = radius_meters / 111000
        min_lat = latitude - delta_deg
        max_lat = latitude + delta_deg
        min_lon = longitude - delta_deg
        max_lon = longitude + delta_deg
        return await self.building_repo.get_all_by_filter_with_options(
            [
                self.building_repo.table.latitude.between(min_lat, max_lat),
                self.building_repo.table.longitude.between(min_lon, max_lon)
            ],
            [
                selectinload(
                    self.building_repo.table.organizations
                ).selectinload(
                    Organization.activities
                ).load_only(Activity.id, Activity.name)
            ]
        )