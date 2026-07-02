from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    id: int
    telegram_id: int
    name: str
    age: int
    weight: float
    height: float
    gender: str
    experience: str
    created_at: datetime
