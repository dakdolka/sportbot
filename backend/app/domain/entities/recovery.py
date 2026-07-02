from dataclasses import dataclass
from datetime import datetime

@dataclass
class Recovery:
    id: int
    user_id: int
    date: datetime
    sleep: float
    hrv: int
    resting_heart_rate: int
    stress: int
    energy: int
    soreness: int
