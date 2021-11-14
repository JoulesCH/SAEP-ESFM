from fastapi import APIRouter

from . import home

api_router = APIRouter()
api_router.include_router(home.router, tags=["Home"])