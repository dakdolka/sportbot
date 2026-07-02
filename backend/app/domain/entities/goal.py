from dataclasses import dataclass
from datetime import datetime

@dataclass
class Goal:
    id: int
    user_id: int
    full_goal: str
    short_goal: str
    created_at: datetime
    updated_at: datetime
