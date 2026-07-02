from dataclasses import dataclass
from datetime import datetime

@dataclass
class TrainingPlan:
    id: int
    user_id: int
    version: int
    current_week: int
    status: str
    plan: dict
    created_at: datetime
    updated_at: datetime
