import pytest
from unittest.mock import MagicMock, patch
from src.game.comida import Comida
from src.game.position import Position
from src.game.food_position_generator import FoodPositionGenerator

# Mocking the Logger to prevent file operations during tests
@pytest.fixture(autouse=True)
def mock_logger():
    with patch('src.game.comida.logger') as mock_log:
        yield mock_log

class TestComida:
    @patch('src.game.comida.FoodPositionGenerator')
    def test_comida_initialization(self, MockFoodPositionGenerator):
        # Configure the mock to return a specific position
        mock_generator_instance = MockFoodPositionGenerator.return_value
        mock_generator_instance.generate_new_position.return_value = Position(50, 50)

        comida = Comida()

        assert comida.getCor() == (255, 0, 0)
        assert comida.getPos() == Position(50, 50)
        mock_generator_instance.generate_new_position.assert_called_once()

    def test_set_get_pos(self):
        comida = Comida()
        new_pos = Position(100, 100)
        comida.setPos(new_pos)
        assert comida.getPos() == new_pos

    @patch('src.game.comida.FoodPositionGenerator')
    def test_new_pos(self, MockFoodPositionGenerator):
        mock_generator_instance = MockFoodPositionGenerator.return_value
        mock_generator_instance.generate_new_position.return_value = Position(70, 70)

        comida = Comida()
        generated_pos = comida.NewPos()

        assert generated_pos == Position(70, 70)
        # Called once during initialization, and once by NewPos()
        assert mock_generator_instance.generate_new_position.call_count == 2
