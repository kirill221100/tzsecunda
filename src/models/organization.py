from typing import List
from sqlalchemy.dialects.postgresql import ARRAY
from src.database import Base
from sqlalchemy.orm import Mapped, relationship, mapped_column
from src.models.organization_activity import organization_activity
from src.utils.custom_types import uuid_pk
from sqlalchemy import String, ForeignKey


class Organization(Base):
    __tablename__ = 'organizations'
    id: Mapped[uuid_pk]
    name: Mapped[str] = mapped_column(nullable=False)
    phone_numbers: Mapped[List[str]] = mapped_column(ARRAY(String), nullable=False)
    building_id: Mapped[str] = mapped_column(ForeignKey('buildings.id'), nullable=False)
    building: Mapped[List["Building"]] = relationship(back_populates="organizations")
    activities: Mapped[List["Activity"]] = relationship(back_populates="organizations", secondary=organization_activity)
