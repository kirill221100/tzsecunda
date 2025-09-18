from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import UUID4
from sqlalchemy.orm import selectinload, deferred
from src import database as db
from src.models import Activity
from src.repositories.organization import OrganisationRepository



class OrganizationService:
    def __init__(self, session: AsyncSession = Depends(db.get_async_session)):
        self.session = session
        self.organization_repo = OrganisationRepository(session=session)

    async def get_all_organizations_by_building_id(self, building_id: UUID4):
        return await self.organization_repo.get_all_by_query(building_id=building_id)

    async def get_all_organizations_by_activities(self, activities: list):
        return await self.organization_repo.get_all_by_filter_with_options(
            filters=[OrganisationRepository.table.activities.any(Activity.id.in_(activities))],
            _options=[
                selectinload(OrganisationRepository.table.activities).load_only(
                    Activity.id, Activity.name
                )
            ]
        )

    async def get_by_id(self, organization_id: UUID4):
        return await self.organization_repo.get_one_by_filter_with_options(
            [
                self.organization_repo.table.id == organization_id
            ],
            [
                selectinload(OrganisationRepository.table.activities).load_only(
                    Activity.id, Activity.name
                ),
                selectinload(OrganisationRepository.table.building)
            ]
        )

    async def get_organizations_by_building(self, building_id: UUID4):
        return await self.organization_repo.get_all_by_filter_with_options(
            [self.organization_repo.table.building_id == building_id],
            [
                selectinload(OrganisationRepository.table.activities).load_only(
                    Activity.id, Activity.name
                )
            ]
        )

    async def get_organizations_by_name(self, name: str):
        return await self.organization_repo.get_all_by_filter_with_options(
            [OrganisationRepository.table.name.ilike(f"%{name}%")],
            [
                selectinload(OrganisationRepository.table.activities).load_only(
                    Activity.id, Activity.name
                )
            ]
        )

