from abc import ABC, abstractmethod
from typing import Optional
from app.domain.entities.training_plan import TrainingPlan

class TrainingRepository(ABC):
    @abstractmethod
    async def create(self, plan: TrainingPlan) -> TrainingPlan:
        pass

    @abstractmethod
    async def get_current(self, user_id: int) -> Optional[TrainingPlan]:
        pass

    @abstractmethod
    async def update(self, plan: TrainingPlan) -> TrainingPlan:
        pass
