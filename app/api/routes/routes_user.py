from fastapi import APIRouter, Depends
from typing import List
from app.schemas.user import UserCreate, UserOut
from app.services.user_service import UserService

router = APIRouter()

@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, service: UserService = Depends()):
    return service.create_user(user)

@router.get("/", response_model=List[UserOut])
def get_users(service: UserService = Depends()):
    return service.get_users()