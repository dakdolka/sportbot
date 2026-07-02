from app.domain.entities.goal import Goal

class GoalService:
    def __init__(self, repos):
        self.repos = repos

    async def create_goal(self, goal: Goal) -> Goal:
        raise NotImplementedError

    async def get_goal(self, goal_id: int) -> Goal:
        raise NotImplementedError

    async def list_goals(self, user_id: int):
        raise NotImplementedError

    async def update_goal(self, goal: Goal) -> Goal:
        raise NotImplementedError

    async def delete_goal(self, goal_id: int) -> None:
        raise NotImplementedError
