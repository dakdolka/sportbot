from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.repositories.training_plan_repository import TrainingPlanRepository as ITrainingPlanRepository
from app.domain.entities.training_plan import TrainingPlan as DomainTrainingPlan
from app.infrastructure.database.models.training_plan import TrainingPlan as TrainingPlanModel

class SQLAlchemyTrainingPlanRepository(ITrainingPlanRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, plan: DomainTrainingPlan) -> DomainTrainingPlan:
        raise NotImplementedError

    async def get_current(self, user_id: int) -> Optional[DomainTrainingPlan]:
        raise NotImplementedError

    async def update(self, plan: DomainTrainingPlan) -> DomainTrainingPlan:
        raise NotImplementedError
