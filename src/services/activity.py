from fastapi import Depends, HTTPException
from pydantic.v1 import UUID4
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from src import database as db
from src.repositories.activity import ActivityRepository


class ActivityService:
    def __init__(self, session: AsyncSession = Depends(db.get_async_session)):
        self.session = session
        self.activity_repo = ActivityRepository(session=session)

    async def get_sub_activities(self, activity_id: UUID4):
        sql = text("""
                WITH RECURSIVE sub AS (
                    SELECT id, parent_id FROM activities WHERE id = :aid
                    UNION
                    SELECT a.id, a.parent_id FROM activities a JOIN sub s ON a.parent_id = s.id
                )
                SELECT id FROM sub;
            """)
        res = (await self.session.execute(sql, {"aid": activity_id})).fetchall()
        return [r[0] for r in res]

