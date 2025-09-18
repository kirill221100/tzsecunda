from typing import List
from src.database import Base
from sqlalchemy.orm import Mapped, relationship, mapped_column
from src.utils.custom_types import uuid_pk

class Building(Base):
    __tablename__ = 'buildings'
    id: Mapped[uuid_pk]
    address: Mapped[str] = mapped_column(nullable=False)
    latitude: Mapped[float] = mapped_column(nullable=False)
    longitude: Mapped[float] = mapped_column(nullable=False)
    organizations: Mapped[List["Organization"]] = relationship(back_populates="building")
