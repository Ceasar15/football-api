from sqlalchemy.orm import Session
from core.schemas import schema
from core.models import models
from fastapi import status
from fastapi import HTTPException


def create(request: schema.User, db: Session):
    user = models.User(name=request.name, nickname=request.nickname)
    db.add(user)
    db.commit()
    db.refresh(user)
    leaderboard = models.LeaderBoard(
        team=request.name,
        played=0,
        won=0,
        draw=0,
        lose=0,
        goals_for=0,
        goals_against=0,
        goals_difference=0,
        points=0,
    )
    db.add(leaderboard)
    db.commit()
    db.refresh(leaderboard)
    return user


def get_all(db: Session):
    users = db.query(models.User).all()
    return users


def get_user_by_id(id, db: Session):
    user = db.query(models.User).get(id)
    if not user:
        raise HTTPException(status_code=404, detail="Team data not found")
    return user
