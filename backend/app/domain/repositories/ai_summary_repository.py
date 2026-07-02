from abc import ABC, abstractmethod
from typing import Optional
from app.domain.entities.ai_summary import AISummary

class AISummaryRepository(ABC):
    @abstractmethod
    async def create(self, summary: AISummary) -> AISummary:
        pass

    @abstractmethod
    async def get_latest(self, user_id: int) -> Optional[AISummary]:
        pass

    @abstractmethod
    async def update(self, summary: AISummary) -> AISummary:
        pass
