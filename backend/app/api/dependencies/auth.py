from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    # Заглушка для авторизации
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not implemented")
