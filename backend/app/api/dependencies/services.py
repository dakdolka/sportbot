from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.dependencies.database import get_db
from app.application.services.repositories import Repositories
from app.application.services.user_service import UserService
from app.application.services.goal_service import GoalService
from app.application.services.training_plan_service import TrainingPlanService
from app.application.services.workout_service import WorkoutService
from app.application.services.recovery_service import RecoveryService

def get_repositories(db: AsyncSession = Depends(get_db)) -> Repositories:
    return Repositories(db)

def get_user_service(repos: Repositories = Depends(get_repositories)) -> UserService:
    return UserService(repos)

def get_goal_service(repos: Repositories = Depends(get_repositories)) -> GoalService:
    return GoalService(repos)

def get_training_plan_service(repos: Repositories = Depends(get_repositories)) -> TrainingPlanService:
    return TrainingPlanService(repos)

def get_workout_service(repos: Repositories = Depends(get_repositories)) -> WorkoutService:
    return WorkoutService(repos)

def get_recovery_service(repos: Repositories = Depends(get_repositories)) -> RecoveryService:
    return RecoveryService(repos)
