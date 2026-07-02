from app.domain.entities.user import User

class UserService:
    def __init__(self, repos):
        self.repos = repos

    async def create_user(self, user: User) -> User:
        raise NotImplementedError

    async def get_user(self, user_id: int) -> User:
        raise NotImplementedError

    async def list_users(self):
        raise NotImplementedError

    async def update_user(self, user: User) -> User:
        raise NotImplementedError

    async def delete_user(self, user_id: int) -> None:
        raise NotImplementedError
