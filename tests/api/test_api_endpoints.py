import json
import os
import pytest
from fastapi.testclient import TestClient
from main import app
from core.database.test_database import test_db

client = TestClient(app)


def test_create_user(test_db):
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
    assert response.status_code == 203


def test_get_leaderboard_success(test_db):
    response = client.get("/statistics/all-leaderboard")
    assert response.status_code == 200


def test_get_stats_of_game(test_db):
    response = client.get("/statistics/get-stats-of-game?game_id=3")
    # assert response.status_code == 200
