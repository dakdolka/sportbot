from app.domain.entities.training_plan import TrainingPlan

class TrainingService:
    def __init__(self, repos):
        self.repos = repos

    async def create_plan(self, plan: TrainingPlan) -> TrainingPlan:
        raise NotImplementedError

    async def get_plan(self, user_id: int) -> TrainingPlan:
        raise NotImplementedError

    async def update_plan(self, plan: TrainingPlan) -> TrainingPlan:
        raise NotImplementedError

    async def get_today_workout(self, user_id: int):
        raise NotImplementedError
