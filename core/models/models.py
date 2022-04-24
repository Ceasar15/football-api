from sqlalchemy import  Column, Integer, String, ForeignKey, Boolean, DateTime
import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from core.database.database import Base

Base = declarative_base()
metadata = Base.metadata

class User(Base):
    __tablename__ = "user"
    id = sa.Column(sa.Integer, primary_key=True, index=True)
    name = sa.Column(sa.String)
    nickname = sa.Column(sa.String)
    is_active = sa.Column(sa.Boolean, default=True)
    leaderboard = relationship("LeaderBoard")

    def __repr__(self):
        return "name: {}, nickname: {}".format(self.name, self.nickname)


class LeaderBoard(Base):
    __tablename__ = "leaderboard"
    id = sa.Column(sa.Integer, primary_key=True, index=True)
    team = sa.Column(sa.String)
    played = sa.Column(sa.Integer)
    won = sa.Column(sa.Integer)
    draw = sa.Column(sa.Integer)
    lose = sa.Column(sa.Integer)
    goals_for = sa.Column(sa.Integer)
    goals_against = sa.Column(sa.Integer)
    goals_difference = sa.Column(sa.Integer)
    points = sa.Column(sa.Integer)
    user_id = sa.Column(sa.Integer, ForeignKey("user.id"))

    def __repr__(self):
        return "team: {}, played: {}, won: {}, lose: {}, points: {}".format(
            self.team, self.played, self.won, self.lose, self.points
        )

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
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
