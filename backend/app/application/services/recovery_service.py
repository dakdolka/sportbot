from app.domain.entities.recovery import Recovery
from datetime import datetime

class RecoveryService:
    def __init__(self, repos):
        self.repos = repos

    async def log_recovery(self, recovery: Recovery) -> Recovery:
        raise NotImplementedError

    async def get_recovery(self, user_id: int, date: datetime) -> Recovery:
        raise NotImplementedError

    async def list_recovery(self, user_id: int):
        raise NotImplementedError
