from fastapi import FastAPI
from app.api.router import api_router
from app.api.handlers import register_exception_handlers
from app.config.settings import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG
)

register_exception_handlers(app)
app.include_router(api_router)
