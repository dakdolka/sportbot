from fastapi import APIRouter
from app.api.responses import ApiResponse

router = APIRouter(tags=["System"])

@router.get("/health", response_model=ApiResponse[dict])
async def health():
    return ApiResponse(ok=True, data={"status": "ok"})
