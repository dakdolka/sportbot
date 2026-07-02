from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.workout import Workout

class WorkoutRepository(ABC):
    @abstractmethod
    async def create(self, workout: Workout) -> Workout:
        pass

    @abstractmethod
    async def get(self, workout_id: int) -> Optional[Workout]:
        pass

    @abstractmethod
    async def list(self, user_id: int) -> List[Workout]:
        pass

    @abstractmethod
    async def delete(self, workout_id: int) -> None:
        pass
