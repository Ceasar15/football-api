import json
import os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from main import app
from core.database.database import get_db, Base

SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()


client = TestClient(app)


def test_create_user():
    data = {
        "id": 0,
        "name": "Test Team",
        "nickname": "Test Nickname",
        "is_active": True
    }
    response = client.post("/users/create_user", json.dumps(data))
    print(response)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 204


def test_get_leaderboard_success():
    response = client.get("/statistics/all-leaderboard")
    assert response.status_code == 200


def test_get_stats_of_game():
    response = client.get("/statistics/get-stats-of-game?game_id=3")
    # assert response.status_code == 200
