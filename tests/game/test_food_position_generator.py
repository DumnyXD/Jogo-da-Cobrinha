import pytest
from unittest.mock import patch, MagicMock
from src.game.food_position_generator import FoodPositionGenerator
from src.game.position import Position
from src.config.game_config import GameConfig

# Mocking the Logger to prevent file operations during tests
@pytest.fixture(autouse=True)
def mock_logger():
    with patch('src.game.food_position_generator.logger') as mock_log:
        yield mock_log

class TestFoodPositionGenerator:
    @patch('random.randrange')
    def test_generate_new_position(self, mock_randrange):
        # Configure mock_randrange to return specific values
        mock_randrange.side_effect = [100, 200] # x=100, y=200

        generator = FoodPositionGenerator()
        pos = generator.generate_new_position()

        assert isinstance(pos, Position)
        assert pos.x == 100
        assert pos.y == 200

        # Verify random.randrange calls
        mock_randrange.assert_any_call(10, GameConfig.largura - 20, 10)
        mock_randrange.assert_any_call(50, GameConfig.altura - 60, 10)
        assert mock_randrange.call_count == 2

    @patch('random.randrange')
    def test_generate_new_position_bounds(self, mock_randrange):
        # Test boundary conditions
        mock_randrange.side_effect = [
            10, 50,  # Min x, Min y
            GameConfig.largura - 20, GameConfig.altura - 60 # Max x, Max y
        ]

        generator = FoodPositionGenerator()

        # Test min bounds
        pos_min = generator.generate_new_position()
        assert pos_min.x == 10
        assert pos_min.y == 50

        # Test max bounds
        pos_max = generator.generate_new_position()
        assert pos_max.x == GameConfig.largura - 20
        assert pos_max.y == GameConfig.altura - 60
