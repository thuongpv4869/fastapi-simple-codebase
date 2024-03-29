from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from app.api.api_v1.api import api_router
from app.config import settings, APP_DIR
from app.middlewares import ProcessTimeMiddleware

app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json")

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
app.add_middleware(ProcessTimeMiddleware)


app.include_router(api_router, prefix=settings.API_V1_STR)

app.mount("/static", StaticFiles(directory=f"{APP_DIR}/{settings.STATIC_DIR}"), name="static")
app.mount("/media", StaticFiles(directory=f"{APP_DIR}/{settings.MEDIA_DIR}"), name="media")
