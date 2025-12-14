from fastapi import APIRouter
from src.services.home_service import HomeService

router=APIRouter()

@router.get("/")
def hello_world():
    return HomeService().hell_world()