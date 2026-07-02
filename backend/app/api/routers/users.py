from fastapi import APIRouter, HTTPException
from app.api.responses import ApiResponse
from typing import Any

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=ApiResponse[Any])
async def list_users():
    raise HTTPException(status_code=501, detail="Not implemented")

@router.get("/{user_id}", response_model=ApiResponse[Any])
async def get_user(user_id: int):
    raise HTTPException(status_code=501, detail="Not implemented")

@router.post("/", response_model=ApiResponse[Any])
async def create_user():
    raise HTTPException(status_code=501, detail="Not implemented")

@router.put("/{user_id}", response_model=ApiResponse[Any])
async def update_user(user_id: int):
    raise HTTPException(status_code=501, detail="Not implemented")

@router.delete("/{user_id}", response_model=ApiResponse[Any])
async def delete_user(user_id: int):
    raise HTTPException(status_code=501, detail="Not implemented")
