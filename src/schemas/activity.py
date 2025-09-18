from pydantic import BaseModel, UUID4


class ActivityBase(BaseModel):
    id: UUID4
    name: str

