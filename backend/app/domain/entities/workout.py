from dataclasses import dataclass
from datetime import datetime

@dataclass
class Workout:
    id: int
    user_id: int
    date: datetime
    duration: float
    distance: float
    pace: float
    avg_heart_rate: int
    max_heart_rate: int
    rpe: int
