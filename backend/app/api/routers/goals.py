from fastapi import APIRouter, HTTPException
from app.api.responses import ApiResponse
from typing import Any

router = APIRouter(prefix="/goals", tags=["Goals"])

@router.get("/", response_model=ApiResponse[Any])
async def list_goals():
    raise HTTPException(status_code=501, detail="Not implemented")

@router.get("/{goal_id}", response_model=ApiResponse[Any])
async def get_goal(goal_id: int):
    raise HTTPException(status_code=501, detail="Not implemented")

@router.post("/", response_model=ApiResponse[Any])
async def create_goal():
    raise HTTPException(status_code=501, detail="Not implemented")

@router.put("/{goal_id}", response_model=ApiResponse[Any])
async def update_goal(goal_id: int):
    raise HTTPException(status_code=501, detail="Not implemented")

@router.delete("/{goal_id}", response_model=ApiResponse[Any])
async def delete_goal(goal_id: int):
    raise HTTPException(status_code=501, detail="Not implemented")
