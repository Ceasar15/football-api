from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from core.database.database import get_db
from core.schemas import schema
from users.endpoints import user
from typing import List

router = APIRouter(tags=["users"], prefix="/users")

# Create User
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.User)
def create_user(request: schema.User, db: Session = Depends(get_db)):
    return user.create(request, db)

# Get Users
@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schema.User])
def get_users(db: Session = Depends(get_db)):
    return user.get_all(db)
