from typing import TypeVar, Generic
from pydantic import BaseModel

T = TypeVar("T")

class ApiResponse(BaseModel, Generic[T]):
    ok: bool
    data: T | None = None
    message: str | None = None
