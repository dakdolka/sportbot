from fastapi import APIRouter, HTTPException
from app.api.responses import ApiResponse
from typing import Any

router = APIRouter(prefix="/training_plan", tags=["TrainingPlan"])

@router.get("/", response_model=ApiResponse[Any])
async def get_plan():
    raise HTTPException(status_code=501, detail="Not implemented")

@router.post("/", response_model=ApiResponse[Any])
async def create_plan():
    raise HTTPException(status_code=501, detail="Not implemented")

@router.put("/", response_model=ApiResponse[Any])
async def update_plan():
    raise HTTPException(status_code=501, detail="Not implemented")

@router.get("/today", response_model=ApiResponse[Any])
async def get_today_workout():
    raise HTTPException(status_code=501, detail="Not implemented")
