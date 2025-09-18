from typing import List
from fastapi import APIRouter, Depends, HTTPException
from pydantic import UUID4
from src.schemas import OrganizationWithActivities, OrganizationWithActivitiesAndBuilding, BuildingWithOrganizations
from src.services.activity import ActivityService
from src.services.building import BuildingService
from src.services.organization import OrganizationService

organization_router = APIRouter(prefix='/organization', tags=['organization'])

@organization_router.get("/get-all-by-activity-id/{activity_id}", response_model=List[OrganizationWithActivities])
async def get_by_activity_id(
        activity_id: UUID4,
        activity_service: "ActivityService" = Depends(ActivityService),
        organization_service: "OrganizationService" = Depends(OrganizationService)
):
    """
    Возвращает организации, принадлежащие к деятельности.
    Например, поиск по виду деятельности «Еда», которая находится на первом уровне дерева, найдет все организации, которые относятся к видам деятельности, лежащим внутри.
    Т.е. в результатах поиска отобразятся организации с видом деятельности Еда, Мясная продукция, Молочная продукция и т.д.
    """
    if activities := await activity_service.get_sub_activities(activity_id):
        return await organization_service.get_all_organizations_by_activities(activities)
    raise HTTPException(404, "Деятельности с таким id не существует")

@organization_router.get("/get-one-by-id/{organization_id}", response_model=OrganizationWithActivitiesAndBuilding)
async def get_organization_by_id(
        organization_id: UUID4,
        organization_service: "OrganizationService" = Depends(OrganizationService)
):
    """
    вывод информации об организации по её идентификатору
    """
    if res := await organization_service.get_by_id(organization_id):
        return res
    raise HTTPException(404, "Организации с таким id не существует")


@organization_router.get("/get-all-by-building/{building_id}", response_model=List[OrganizationWithActivities])
async def get_organizations_by_building(
        building_id: UUID4,
        building_service: "BuildingService" = Depends(BuildingService),
):
    """
    список всех организаций находящихся в конкретном здании
    """
    if building := await building_service.get_with_organizations(building_id):
        return building.organizations
    raise HTTPException(404, "Здания с таким id не существует")

@organization_router.get("/get-all-by-name", response_model=List[OrganizationWithActivities])
async def get_all_by_name(
        name: str,
        organization_service: "OrganizationService" = Depends(OrganizationService)
):
    """
    поиск организации по названию
    """
    return await organization_service.get_organizations_by_name(name)

@organization_router.get("/get-all-within-radius", response_model=List[BuildingWithOrganizations])
async def get_all_within_radius(
        latitude: float,
        longitude: float,
        radius_meters: int,
        building_service: "BuildingService" = Depends(BuildingService)
):
    """
    список организаций, которые находятся в заданном радиусе/прямоугольной области относительно указанной точки на карте
    """
    return await building_service.get_all_within_radius(latitude, longitude, radius_meters)
