from .v1.organization import organization_router
from fastapi import APIRouter

v1_router = APIRouter(prefix='/api/v1')
v1_router.include_router(organization_router)