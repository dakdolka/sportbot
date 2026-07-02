from app.domain.entities.workout import Workout

class WorkoutService:
    def __init__(self, repos):
        self.repos = repos

    async def log_workout(self, workout: Workout) -> Workout:
        raise NotImplementedError

    async def get_workout(self, workout_id: int) -> Workout:
        raise NotImplementedError

    async def list_workouts(self, user_id: int):
        raise NotImplementedError

    async def delete_workout(self, workout_id: int) -> None:
        raise NotImplementedError
