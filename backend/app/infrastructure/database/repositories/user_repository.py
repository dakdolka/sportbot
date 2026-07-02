from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.repositories.user_repository import UserRepository as IUserRepository
from app.domain.entities.user import User as DomainUser
from app.infrastructure.database.models.user import User as UserModel

class SQLAlchemyUserRepository(IUserRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, user: DomainUser) -> DomainUser:
        raise NotImplementedError

    async def get(self, user_id: int) -> Optional[DomainUser]:
        raise NotImplementedError

    async def list(self) -> List[DomainUser]:
        raise NotImplementedError

    async def update(self, user: DomainUser) -> DomainUser:
        raise NotImplementedError

    async def delete(self, user_id: int) -> None:
        raise NotImplementedError
