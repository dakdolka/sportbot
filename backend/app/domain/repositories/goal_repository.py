from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.goal import Goal

class GoalRepository(ABC):
    @abstractmethod
    async def create(self, goal: Goal) -> Goal:
        pass

    @abstractmethod
    async def get(self, goal_id: int) -> Optional[Goal]:
        pass

    @abstractmethod
    async def list(self, user_id: int) -> List[Goal]:
        pass

    @abstractmethod
    async def update(self, goal: Goal) -> Goal:
        pass

    @abstractmethod
    async def delete(self, goal_id: int) -> None:
        pass
