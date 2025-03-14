from fastapi import APIRouter
from .endpoints import users

api_router = APIRouter()
api_router.include_router(users.router, tags=["users"])
