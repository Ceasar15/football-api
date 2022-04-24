from sqlalchemy.orm import Session
from core.schemas import schema
from core.models import models
from fastapi import HTTPException


# Get leaderboard
def get_leaderboard(db: Session):
    leaderboard = db.query(models.LeaderBoard).all()
    leaderboard.sort(
        key=lambda x: (x.points, x.goals_difference, x.goals_for), reverse=True
    )
    return leaderboard


#  create stats per game
def create_stats_per_game(request: schema.StatsSheetSchema, db: Session):
    # check if teams exists in db
    home_team_leaderboard = (
        db.query(models.LeaderBoard)
        .filter(models.LeaderBoard.team == request.home_team)
        .first()
    )
    if not home_team_leaderboard:
        raise HTTPException(status_code=404, detail="Home Team data not found")
    away_team_leaderboard = (
        db.query(models.LeaderBoard)
        .filter(models.LeaderBoard.team == request.away_team)
        .first()
    )
    if not away_team_leaderboard:
        raise HTTPException(status_code=404, detail="Away Team data not found")

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
    db.add(stats_per_game)
    db.commit()
    db.refresh(stats_per_game)

    # increase game played
    home_team_leaderboard.played += 1
    away_team_leaderboard.played += 1
    #  calculate goals scored for, against and difference
    home_team_leaderboard.goals_for += int(request.home_team_goals)
    away_team_leaderboard.goals_for += int(request.away_team_goals)
    home_team_leaderboard.goals_against += int(request.away_team_goals)
    away_team_leaderboard.goals_against += int(request.home_team_goals)

    # check for wins and losses
    if request.home_team_goals > request.away_team_goals:
        home_team_leaderboard.won += 1
        home_team_leaderboard.points += 3
        away_team_leaderboard.lose += 1
    elif request.home_team_goals < request.away_team_goals:
        away_team_leaderboard.won += 1
        away_team_leaderboard.points += 3
        home_team_leaderboard.lose += 1
    else:
        home_team_leaderboard.points += 1
        away_team_leaderboard.points += 1
        home_team_leaderboard.draw += 1
        away_team_leaderboard.draw += 1

    db.add_all([home_team_leaderboard, away_team_leaderboard])
    db.commit()
    db.refresh(home_team_leaderboard)
    home_team_leaderboard.goals_difference = (
        home_team_leaderboard.goals_for - home_team_leaderboard.goals_against
    )
    away_team_leaderboard.goals_difference = (
        away_team_leaderboard.goals_for - away_team_leaderboard.goals_against
    )
    db.add_all([home_team_leaderboard, away_team_leaderboard])
    db.commit()
    db.refresh(away_team_leaderboard)

    return stats_per_game


def get_all_stats(db: Session):
    all_stats = db.query(models.StatsSheet).all()
    return all_stats


def get_game_stats_of_a_team(db: Session):
    team_stats = db.query(models.StatsSheet.home_team).filter(
        models.StatsSheet.home_team == "Team One"
    )
    if not team_stats:
        raise HTTPException(status_code=404, detail="Team data not found")
    return team_stats


def get_leaderboard_of_a_team(team_name, db: Session):
    leaderboard_of_team = (
        db.query(models.LeaderBoard)
        .filter(models.LeaderBoard.team == team_name)
        .first()
    )
    if not leaderboard_of_team:
        raise HTTPException(status_code=404, detail="Team data not found")
    return leaderboard_of_team
