from pydantic import BaseModel
from typing import Optional
from datetime import datetime, time, timedelta


class UserBase(BaseModel):
    id: int
    name: str
    nickname: str
    is_active: bool


class User(UserBase):
    class Config:
        orm_mode = True


class LeaderBoardBase(BaseModel):
    id: int
    team: str
    played: int
    won: int
    draw: int
    lose: int
    goals_for: int
    goals_against: int
    goals_difference: int
    points: int

    class Config:
        orm_mode = True


class StatsSheetSchema(BaseModel):
    home_team: str
    away_team: str
    home_team_goals: int
    away_team_goals: int
    home_team_possession: int
    away_team_possession: int
    home_team_fouls: int
    away_team_fouls: int
    home_team_yellow_cards: int
    away_team_yellow_cards: int
    home_team_red_cards: int
    away_team_red_cards: int

    class Config:
        orm_mode = True


class ShowStatsSheet(BaseModel):
    id: Optional[int]
    home_team: Optional[str]
    away_team: Optional[str]
    home_team_goals: Optional[int]
    away_team_goals: Optional[int]
    time_created: Optional[datetime]
    home_team_possession: Optional[int]
    away_team_possession: Optional[int]
    home_team_fouls: Optional[int]
    away_team_fouls: Optional[int]
    home_team_yellow_cards: Optional[int]
    away_team_yellow_cards: Optional[int]
    home_team_red_cards: Optional[int]
    away_team_red_cards: Optional[int]

    class Config:
        orm_mode = True
