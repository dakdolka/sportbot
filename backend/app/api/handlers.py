from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.api.exceptions import ApiException

def register_exception_handlers(app: FastAPI):
    @app.exception_handler(ApiException)
    async def api_exception_handler(request: Request, exc: ApiException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"ok": False, "data": None, "message": exc.message}
        )
