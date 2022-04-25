from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK

from api import api
from core.database.database import get_db
from core.schemas import schema

router = APIRouter(tags=["statistics"], prefix="/statistics")


# Get all leaderboard
@router.get("/all-leaderboard", status_code=status.HTTP_200_OK, response_model=List[schema.LeaderBoardBase])
def get_users(db: Session = Depends(get_db)):
    return api.get_leaderboard(db)


#  get leader scores for a team
@router.get("/get_leaderboard_of_a_team", status_code=status.HTTP_200_OK, response_model=schema.LeaderBoardBase)
def get_users(team_name: str, db: Session = Depends(get_db)):
    return api.get_leaderboard_of_a_team(team_name, db)


# create stats for a game
@router.post("/create-stats-of-game", status_code=status.HTTP_201_CREATED, response_model=schema.StatsSheetSchema)
def create_stats_per_game(request: schema.StatsSheetSchema, db: Session = Depends(get_db)):
    return api.create_stats_per_game(request, db)


# get stats of a game
@router.post("/get-stats-of-game", status_code=status.HTTP_200_OK)
def get_stats_of_game(game_id: int, db: Session = Depends(get_db)):
    return api.get_stats_per_game(game_id, db)


# update stats of a game
@router.put("/update-stats-of-game", status_code=HTTP_200_OK, response_model=schema.ShowStatsSheet)
def update_stats_of_game(game_id, request: schema.StatsSheetSchema, db: Session = Depends(get_db)):
    return api.update_stats_per_game(game_id, request, db)


# delete stats of a game
@router.delete("/delete-stats-of-game", status_code=status.HTTP_200_OK)
def delete_stats_of_game(game_id: int, db: Session = Depends(get_db)):
    return api.delete_stats_per_game(game_id, db)


# Get stats for all games
@router.get("/get_all_stats", status_code=status.HTTP_200_OK, response_model=List[schema.ShowStatsSheet])
def get_stats_for_games(db: Session = Depends(get_db)):
    return api.get_all_stats(db)


# Get stats for a team
@router.get("/get_stats_for_team", status_code=status.HTTP_200_OK, response_model=List[schema.ShowStatsSheet])
def get_stats_for_team(team_name: str, db: Session = Depends(get_db)):
    return api.get_game_stats_of_a_team(team_name, db)
