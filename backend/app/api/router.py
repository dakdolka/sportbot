from fastapi import APIRouter
from app.api.routers import system, users, goals, training_plan, workouts, recovery

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(system.router)
api_router.include_router(users.router)
api_router.include_router(goals.router)
api_router.include_router(training_plan.router)
api_router.include_router(workouts.router)
api_router.include_router(recovery.router)
