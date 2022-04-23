from core.database.database import Base, engine
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    nickname = Column(String)
    is_active = Column(Boolean, default=True)


class LeaderBoard(Base):
    __tablename__ = "leaderboard"
    id = Column(Integer, primary_key=True, index=True)
    team = Column(String)
    played = Column(Integer)
    won = Column(Integer)
    lose = Column(Integer)
    points = Column(Integer)


class StatsSheet(Base):
    __tablename__ = "stats_sheet"
    id = Column(Integer, primary_key=True, index=True)
    home_team = Column(String)
    away_team = Column(String)
    home_team_goals = Column(Integer)
    away_team_goals = Column(Integer)
    home_team_possession = Column(Integer)
    away_team_possession = Column(Integer)
    home_team_fouls = Column(Integer)
    away_team_fouls = Column(Integer)
    home_team_yellow_cards = Column(Integer)
    away_team_yellow_cards = Column(Integer)
    home_team_red_cards = Column(Integer)
    away_team_red_cards = Column(Integer)


Base.metadata.create_all(engine, Base.metadata.tables.values(), checkfirst=True)
