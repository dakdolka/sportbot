from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.repositories.user_repository import SQLAlchemyUserRepository
from app.infrastructure.repositories.goal_repository import SQLAlchemyGoalRepository
from app.infrastructure.repositories.training_repository import SQLAlchemyTrainingRepository
from app.infrastructure.repositories.workout_repository import SQLAlchemyWorkoutRepository
from app.infrastructure.repositories.recovery_repository import SQLAlchemyRecoveryRepository
from app.infrastructure.repositories.ai_summary_repository import SQLAlchemyAISummaryRepository

class Repositories:
    def __init__(self, db: AsyncSession):
        self.user = SQLAlchemyUserRepository(db)
        self.goal = SQLAlchemyGoalRepository(db)
        self.training = SQLAlchemyTrainingRepository(db)
        self.workout = SQLAlchemyWorkoutRepository(db)
        self.recovery = SQLAlchemyRecoveryRepository(db)
        self.ai_summary = SQLAlchemyAISummaryRepository(db)
