from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.repositories.recovery_repository import RecoveryRepository as IRecoveryRepository
from app.domain.entities.recovery import Recovery as DomainRecovery
from app.infrastructure.database.models.recovery import Recovery as RecoveryModel

class SQLAlchemyRecoveryRepository(IRecoveryRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, recovery: DomainRecovery) -> DomainRecovery:
        raise NotImplementedError

    async def get(self, user_id: int, date: 'datetime') -> Optional[DomainRecovery]:
        raise NotImplementedError

    async def list(self, user_id: int) -> List[DomainRecovery]:
        raise NotImplementedError

    async def update(self, recovery: DomainRecovery) -> DomainRecovery:
        raise NotImplementedError
