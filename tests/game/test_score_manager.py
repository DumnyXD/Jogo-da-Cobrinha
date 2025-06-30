import pytest
from unittest.mock import patch
from src.game.score_manager import ScoreManager

# Mocking the Logger to prevent file operations during tests
@pytest.fixture(autouse=True)
def mock_logger():
    with patch('src.game.score_manager.logger') as mock_log:
        yield mock_log

class TestScoreManager:
    def test_initialization(self):
        score_manager = ScoreManager(100)
        assert score_manager.get_current_score() == 0
        assert score_manager.get_high_score() == 100

    def test_add_score(self):
        score_manager = ScoreManager(0)
        score_manager.add_score(10)
        assert score_manager.get_current_score() == 10
        assert score_manager.get_high_score() == 10

        score_manager.add_score(5)
        assert score_manager.get_current_score() == 15
        assert score_manager.get_high_score() == 15

    def test_add_score_high_score_not_exceeded(self):
        score_manager = ScoreManager(20)
        score_manager.add_score(10)
        assert score_manager.get_current_score() == 10
        assert score_manager.get_high_score() == 20

    def test_reset_score(self):
        score_manager = ScoreManager(100)
        score_manager.add_score(50)
        assert score_manager.get_current_score() == 50
        score_manager.reset_score()
        assert score_manager.get_current_score() == 0
        assert score_manager.get_high_score() == 100 # High score should not reset

    def test_get_current_score(self):
        score_manager = ScoreManager(0)
        score_manager.add_score(25)
        assert score_manager.get_current_score() == 25

    def test_get_high_score(self):
        score_manager = ScoreManager(50)
        score_manager.add_score(10)
        assert score_manager.get_high_score() == 50
        score_manager.add_score(50)
        assert score_manager.get_high_score() == 60
