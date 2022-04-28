import json
from fastapi.testclient import TestClient
from main import app
from core.database.test_database import test_db

client = TestClient(app)


def test_create_user(test_db):
    data1 = {
        "id": 0,
        "name": "Test Ars",
        "nickname": "Test Nickname1",
        "is_active": True
    }
    data2 = {
        "id": 0,
        "name": "Test Ches",
        "nickname": "Test Nickname2",
        "is_active": True
    }
    response1 = client.post("/users/create_user", json.dumps(data1))
    assert response1.status_code == 201

    response2 = client.post("/users/create_user", json.dumps(data2))
    assert response2.status_code == 201


def test_get_all_users(test_db):
    response = client.get("/users/get_all_users")
    assert response.status_code == 200
    assert (response.json()) is not None


def test_get_user_by_id(test_db):
    response = client.get("/users/get_user_by_id/1")
    expected_response = {'id': 1, 'name': 'Test Team2', 'nickname': 'Test Nickname1', 'is_active': True}
    assert response.status_code == 200
    assert (response.json()) == expected_response


def test_get_leaderboard_success(test_db):
    response = client.get("/statistics/all-leaderboard")
    assert response.status_code == 200


def test_get_leaderboard_of_a_team_success(test_db):
    response = client.get("statistics/get_leaderboard_of_a_team?team_name=Test Team2")
    expected_response = {'id': 1, 'team': 'Test Team2', 'played': 0, 'won': 0, 'draw': 0, 'lose': 0, 'goals_for': 0,
                         'goals_against': 0, 'goals_difference': 0, 'points': 0}
    assert response.status_code == 200
    assert response.json() == expected_response


def test_get_leaderboard_of_a_team_failure(test_db):
    response = client.get("statistics/get_leaderboard_of_a_team?team_name=Team%20One")
    expected_response = {'detail': 'Team data not found'}
    assert response.status_code == 404
    assert response.json() == expected_response


def test_create_stats_per_game(test_db):
    stats_per_game = {
        "home_team": "Test Ars",
        "away_team": "Test Ches",
        "home_team_goals": 3,
        "away_team_goals": 4,
        "home_team_possession": 50,
        "away_team_possession": 50,
        "home_team_fouls": 6,
        "away_team_fouls": 5,
        "home_team_yellow_cards": 4,
        "away_team_yellow_cards": 2,
        "home_team_red_cards": 1,
        "away_team_red_cards": 1
    }
    response = client.post("/statistics/create-stats-of-game", json.dumps(stats_per_game))
    expected_response = {'home_team': 'Test Ars', 'away_team': 'Test Ches', 'home_team_goals': 3, 'away_team_goals': 4,
                         'home_team_possession': 50, 'away_team_possession': 50, 'home_team_fouls': 6,
                         'away_team_fouls': 5, 'home_team_yellow_cards': 4, 'away_team_yellow_cards': 2,
                         'home_team_red_cards': 1, 'away_team_red_cards': 1}
    assert response.status_code == 201
    assert response.json() == expected_response


def test_get_all_stats(test_db):
    response = client.get("statistics/get_all_stats")
    assert response.status_code == 200
    assert response.json() is not None


def test_get_stats_for_team(test_db):
    response = client.get("statistics/get_stats_for_team?team_name=Test Ars")
    assert response.status_code == 200
    assert response.json() is not None


def test_get_stats_of_game_exist(test_db):
    response = client.post("/statistics/get-stats-of-game?game_id=1")
    expected_response = {'home_team': 'Test Ars', 'away_team_goals': 4, 'home_team_goals': 3,
                         'away_team_possession': 50, 'away_team_fouls': 5, 'away_team_yellow_cards': 2,
                         'away_team_red_cards': 1, 'time_updated': None, 'away_team': 'Test Ches', 'id': 1,
                         'home_team_possession': 50, 'home_team_fouls': 6, 'home_team_yellow_cards': 4,
                         'home_team_red_cards': 1, 'time_created': '2022-04-27T08:12:47.311715+00:00'}
    assert response.status_code == 200
    assert response.json() == expected_response


def test_get_stats_of_game_does_not_exist(test_db):
    response = client.post("/statistics/get-stats-of-game?game_id=90900")
    expected_response = {'detail': 'This game does not exist'}
    assert response.status_code == 404
    assert response.json() == expected_response
