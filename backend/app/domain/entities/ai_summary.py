from dataclasses import dataclass
from datetime import datetime

@dataclass
class AISummary:
    id: int
    user_id: int
    summary: str
    updated_at: datetime
