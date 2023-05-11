from fastapi import APIRouter

from app.api.api_v1.endpoints import (
    customers,
    authen,
    users
)

api_router = APIRouter()

api_router.include_router(authen.router, prefix="", tags=["authentication"])
api_router.include_router(customers.router, prefix="/customers", tags=["customers"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
