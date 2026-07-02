from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime
from app.domain.entities.recovery import Recovery

class RecoveryRepository(ABC):
    @abstractmethod
    async def create(self, recovery: Recovery) -> Recovery:
        pass

    @abstractmethod
    async def get(self, user_id: int, date: datetime) -> Optional[Recovery]:
        pass

    @abstractmethod
    async def list(self, user_id: int) -> List[Recovery]:
        pass

    @abstractmethod
    async def update(self, recovery: Recovery) -> Recovery:
        pass
