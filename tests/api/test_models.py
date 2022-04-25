from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_leaderboard_success():
    response = client.get("/statistics/all-leaderboard")
    assert response.status_code == 200


def test_get_stats_of_game():
    response = client.get("/statistics/get-stats-of-game?game_id=3")
    assert response.status_code == 200
