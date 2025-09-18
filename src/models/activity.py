from typing import List
from sqlalchemy import ForeignKey
from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.organization_activity import organization_activity
from src.utils.custom_types import uuid_pk

class Activity(Base):
    __tablename__ = 'activities'
    id: Mapped[uuid_pk]
    name: Mapped[str] = mapped_column(nullable=False)
    parent_id: Mapped[str] = mapped_column(ForeignKey("activities.id"), nullable=True)
    parent: Mapped["Activity"] = relationship(remote_side="Activity.id", backref="children")
    organizations: Mapped[List["Organization"]] = relationship(back_populates="activities", secondary=organization_activity)
