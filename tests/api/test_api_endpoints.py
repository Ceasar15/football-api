import json
import os
import pytest
from fastapi.testclient import TestClient
from main import app
from core.database.test_database import test_db

client = TestClient(app)


def test_create_user(test_db):
    data1 = {
        "id": 0,
        "name": "Test Team2",
        "nickname": "Test Nickname1",
        "is_active": True
    }
    data2 = {
        "id": 0,
        "name": "Test Team2",
        "nickname": "Test Nickname2",
        "is_active": True
    }
    response1 = client.post("/users/create_user", json.dumps(data1))
    assert response1.status_code == 201

    response2 = client.post("/users/create_user", json.dumps(data2))
    assert response2.status_code == 201


def test_get_all_users(test_db):
    response = client.get("/users/get_all_users")
    print(45454545454, response.json())
    print(9999999999, len(response.json()))
    assert response.status_code == 404


def test_get_leaderboard_success(test_db):
    response = client.get("/statistics/all-leaderboard")
    assert response.status_code == 200


def test_get_stats_of_game_exist(test_db):
    response = client.post("/statistics/get-stats-of-game?game_id=1")
    assert response.status_code == 200


def test_get_stats_of_game_does_not_exist(test_db):
    response = client.post("/statistics/get-stats-of-game?game_id=3")
    assert response.status_code == 404
