from fastapi import APIRouter, HTTPException
from app.api.responses import ApiResponse
from typing import Any

router = APIRouter(prefix="/workouts", tags=["Workouts"])

@router.get("/", response_model=ApiResponse[Any])
async def list_workouts():
    raise HTTPException(status_code=501, detail="Not implemented")

@router.get("/{workout_id}", response_model=ApiResponse[Any])
async def get_workout(workout_id: int):
    raise HTTPException(status_code=501, detail="Not implemented")

@router.post("/", response_model=ApiResponse[Any])
async def create_workout():
    raise HTTPException(status_code=501, detail="Not implemented")

@router.put("/{workout_id}", response_model=ApiResponse[Any])
async def update_workout(workout_id: int):
    raise HTTPException(status_code=501, detail="Not implemented")

@router.delete("/{workout_id}", response_model=ApiResponse[Any])
async def delete_workout(workout_id: int):
    raise HTTPException(status_code=501, detail="Not implemented")
