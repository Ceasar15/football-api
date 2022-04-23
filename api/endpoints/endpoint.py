from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from core.database.database import get_db
from core.schemas import schema
from typing import List
from api import api

router = APIRouter(tags=["statistics"], prefix="/statistics")


@router.get("/first")
def api_home():
    return {"second": "endpoint"}

# Create leaderboard
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.LeaderBoardBase)
def create_user(request: schema.LeaderBoardBase, db: Session = Depends(get_db)):
    return api.create(request, db)

# Get all leaderboard
@router.get("/all-leaderboard", status_code=status.HTTP_200_OK, response_model=List[schema.StatsSheetSchema])
def get_users(db: Session = Depends(get_db)):
    return api.get_leaderboard(db)

# create stats for a game
@router.post("/create-stats-of-game", status_code=status.HTTP_201_CREATED, response_model=schema.StatsSheetSchema)
def create_stats_per_game(request: schema.StatsSheetSchema, db: Session = Depends(get_db)):
    return api.create_stats_per_game(request, db)

# Get stats for all game
@router.get("/get_all_stats", status_code=status.HTTP_200_OK, response_model=List[schema.StatsSheetSchema])
def get_all_stats(db: Session = Depends(get_db)):
    return api.get_all_stats(db)