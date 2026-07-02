from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.repositories.ai_summary_repository import AISummaryRepository as IAISummaryRepository
from app.domain.entities.ai_summary import AISummary as DomainAISummary
from app.infrastructure.database.models.ai_summary import AISummary as AISummaryModel

class SQLAlchemyAISummaryRepository(IAISummaryRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, summary: DomainAISummary) -> DomainAISummary:
        raise NotImplementedError

    async def get_latest(self, user_id: int) -> Optional[DomainAISummary]:
        raise NotImplementedError

    async def update(self, summary: DomainAISummary) -> DomainAISummary:
        raise NotImplementedError
