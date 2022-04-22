from sqlalchemy.orm import Session
from core.schemas import schema
from core.models import models
from fastapi import status


def create(request: schema.User, db: Session):
    user = models.User(name=request.name, nickname=request.nickname)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_all(db: Session):
    users = db.query(models.User).all()
    return users