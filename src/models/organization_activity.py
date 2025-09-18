from sqlalchemy import Column, String, ForeignKey, Table, UUID

from src.database import Base

organization_activity = Table(
    "organization_activity",
    Base.metadata,
    Column("organization_id", UUID, ForeignKey("organizations.id"), primary_key=True),
    Column("activity_id", UUID, ForeignKey("activities.id"), primary_key=True)
)