from sqlalchemy.orm import Session
from core.schemas import schema
from core.models import models
from fastapi import FastAPI, HTTPException

def create(request: schema.User, db: Session):
    leaderboard = models.LeaderBoard(
        played=request.played, won=request.won, lose=request.lose
    )
    db.add(leaderboard)
    db.commit()
    db.refresh(leaderboard)
    return leaderboard


def get_leaderboard(db: Session):
    leaderboard = db.query(models.StatsSheet).all()
    for i in leaderboard:
        print(1, dir(i))
        print(2, i.home_team)
    return leaderboard


def create_stats_per_game(request: schema.StatsSheetSchema, db: Session):
    stats_per_game = models.StatsSheet(
        home_team=request.home_team,
        away_team=request.away_team,
        home_team_goals=request.home_team_goals,
        away_team_goals=request.away_team_goals,
        home_team_possession=request.home_team_possession,
        away_team_possession=request.away_team_possession,
        home_team_fouls=request.home_team_fouls,
        away_team_fouls=request.away_team_fouls,
        home_team_yellow_cards=request.home_team_yellow_cards,
        away_team_yellow_cards=request.away_team_yellow_cards,
        home_team_red_cards=request.home_team_red_cards,
        away_team_red_cards=request.away_team_red_cards,
    )
    # db.add(stats_per_game)
    # db.commit()
    # db.refresh(stats_per_game)
    db_hero = db.query(models.LeaderBoard).filter(models.LeaderBoard.team==request.home_team)
    if not db_hero:
        raise HTTPException(status_code=404, detail="Data not found")
    print(33, db_hero)
    instance1 = models.LeaderBoard(
        team=request.home_team, played=1, won=1, lose=0, points=3
    )
    instance2 = models.LeaderBoard(
        team=request.away_team, played=1, won=1, lose=0, points=0
    )
    # db.add_all([instance1, instance2])
    # db.commit()
    # db.refresh(instance1)
    return stats_per_game


def get_all_stats(db: Session):
    leaderboard = db.query(models.StatsSheet).all()
    return leaderboard
