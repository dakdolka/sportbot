from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.repositories.goal_repository import GoalRepository as IGoalRepository
from app.domain.entities.goal import Goal as DomainGoal
from app.infrastructure.database.models.goal import Goal as GoalModel

class SQLAlchemyGoalRepository(IGoalRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, goal: DomainGoal) -> DomainGoal:
        raise NotImplementedError

    async def get(self, goal_id: int) -> Optional[DomainGoal]:
        raise NotImplementedError

    async def list(self, user_id: int) -> List[DomainGoal]:
        raise NotImplementedError

    async def update(self, goal: DomainGoal) -> DomainGoal:
        raise NotImplementedError

    async def delete(self, goal_id: int) -> None:
        raise NotImplementedError
