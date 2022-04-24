import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

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
    user_id = sa.Column(sa.Integer, sa.ForeignKey("user.id"))

    def __repr__(self):
        return "team: {}, played: {}, won: {}, lose: {}, points: {}".format(
            self.team, self.played, self.won, self.lose, self.points
        )


class StatsSheet(Base):
    __tablename__ = "stats_sheet"
    id = sa.Column(sa.Integer, primary_key=True, index=True)
    home_team = sa.Column(sa.String)
    away_team = sa.Column(sa.String)
    home_team_goals = sa.Column(sa.Integer)
    away_team_goals = sa.Column(sa.Integer)
    home_team_possession = sa.Column(sa.Integer)
    away_team_possession = sa.Column(sa.Integer)
    home_team_fouls = sa.Column(sa.Integer)
    away_team_fouls = sa.Column(sa.Integer)
    home_team_yellow_cards = sa.Column(sa.Integer)
    away_team_yellow_cards = sa.Column(sa.Integer)
    home_team_red_cards = sa.Column(sa.Integer)
    away_team_red_cards = sa.Column(sa.Integer)
    time_created = sa.Column(sa.DateTime(timezone=True), server_default=func.now())
    time_updated = sa.Column(sa.DateTime(timezone=True), onupdate=func.now())
