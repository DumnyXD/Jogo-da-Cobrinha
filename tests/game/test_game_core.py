import pytest
from unittest.mock import MagicMock, patch
from src.game.game_core import GameCore
from src.game.cobrinha import Cobrinha
from src.game.comida import Comida
from src.game.score_manager import ScoreManager
from src.game.game_observer import GameObserver
from src.game.position import Position
from src.config.game_config import GameConfig

# Mocking external dependencies
@pytest.fixture
def mock_cobrinha():
    mock = MagicMock(spec=Cobrinha)
    mock.getPosCabeca.return_value = Position(100, 100)
    mock.getPerca.return_value = True
    mock.getDirecao.return_value = None
    return mock

@pytest.fixture
def mock_comida():
    mock = MagicMock(spec=Comida)
    mock.getPos.return_value = Position(100, 100) # Initial food position for tests
    mock.NewPos.return_value = Position(200, 200) # New food position after consumption
    return mock

@pytest.fixture
def mock_score_manager():
    mock = MagicMock(spec=ScoreManager)
    mock.get_current_score.return_value = 0
    mock.get_high_score.return_value = 0
    return mock

@pytest.fixture
def mock_logger():
    with patch('src.game.game_core.logger') as mock_log:
        yield mock_log

@pytest.fixture
def mock_game_observer():
    return MagicMock(spec=GameObserver)

class TestGameCore:
    def test_game_core_initialization(self, mock_cobrinha, mock_comida, mock_score_manager, mock_logger):
        with (patch('src.game.game_core.Cobrinha', return_value=mock_cobrinha),
              patch('src.game.game_core.Comida', return_value=mock_comida),
              patch('src.game.game_core.ScoreManager', return_value=mock_score_manager)):
            game_core = GameCore(100)

            assert game_core.score_manager == mock_score_manager
            assert game_core.comida == mock_comida
            assert game_core.cobrinha == mock_cobrinha
            assert game_core.pausado is False
            assert game_core._observers == []
            mock_logger.info.assert_called_with("GameCore inicializado.")

    def test_add_remove_observer(self, mock_game_observer):
        game_core = GameCore(0)
        game_core.add_observer(mock_game_observer)
        assert mock_game_observer in game_core._observers

        game_core.remove_observer(mock_game_observer)
        assert mock_game_observer not in game_core._observers

    def test_notify_observers(self, mock_game_observer):
        game_core = GameCore(0)
        game_core.add_observer(mock_game_observer)
        game_core._notify_observers()
        mock_game_observer.update.assert_called_once_with(game_core.get_game_state())

    def test_update_toggle_pause(self, mock_logger):
        game_core = GameCore(0)
        game_core.update(["toggle_pause"])
        assert game_core.pausado is True
        mock_logger.info.assert_any_call("Jogo PAUSADO.")

        game_core.update(["toggle_pause"])
        assert game_core.pausado is False
        mock_logger.info.assert_any_call("Jogo RESUMIDO.")

    @pytest.mark.parametrize("initial_direction, action, should_change, new_direction", [
        (None, "move_up", True, "cima"),
        ("direita", "move_up", True, "cima"),
        ("cima", "move_down", False, None), # Invalid change
        (None, "move_down", True, "baixo"),
        ("cima", "move_down", False, None), # Invalid change
        ("baixo", "move_up", False, None), # Invalid change
        (None, "move_left", True, "esquerda"),
        ("cima", "move_left", True, "esquerda"),
        ("direita", "move_left", False, None), # Invalid change
        (None, "move_right", True, "direita"),
        ("cima", "move_right", True, "direita"),
        ("esquerda", "move_right", False, None), # Invalid change
    ])
    def test_update_direction_change(self, mock_cobrinha, mock_logger, initial_direction, action, should_change, new_direction):
        mock_cobrinha.getDirecao.return_value = initial_direction
        game_core = GameCore(0)
        game_core.cobrinha = mock_cobrinha # Assign mock to game_core

        game_core.update([action])

        if should_change:
            mock_cobrinha.setDirecao.assert_called_with(new_direction)
        else:
            mock_cobrinha.setDirecao.assert_not_called()

    def test_update_food_consumption(self, mock_cobrinha, mock_comida, mock_score_manager, mock_logger):
        mock_cobrinha.getPosCabeca.return_value = Position(100, 100)
        mock_comida.getPos.return_value = Position(100, 100) # Food at snake's head
        mock_score_manager.get_current_score.return_value = 0

        game_core = GameCore(0)
        game_core.cobrinha = mock_cobrinha
        game_core.comida = mock_comida
        game_core.score_manager = mock_score_manager

        game_core.update([]) # No action, just update game state

        mock_score_manager.add_score.assert_called_with(10)
        mock_comida.NewPos.assert_called_once()
        mock_comida.setPos.assert_called_with(Position(200, 200)) # NewPos return value
        mock_cobrinha.Move.assert_called_with(True) # Snake should grow
        mock_logger.info.assert_any_call("Comida consumida!")

    def test_update_no_food_consumption(self, mock_cobrinha, mock_comida, mock_score_manager, mock_logger):
        mock_cobrinha.getPosCabeca.return_value = Position(100, 100)
        mock_comida.getPos.return_value = Position(150, 150) # Food not at snake's head

        game_core = GameCore(0)
        game_core.cobrinha = mock_cobrinha
        game_core.comida = mock_comida
        game_core.score_manager = mock_score_manager

        game_core.update([])

        mock_score_manager.add_score.assert_not_called()
        mock_comida.NewPos.assert_not_called()
        mock_comida.setPos.assert_not_called()
        mock_cobrinha.Move.assert_called_with(False) # Snake should not grow

    def test_update_game_over(self, mock_cobrinha, mock_score_manager, mock_logger):
        mock_cobrinha.getPerca.return_value = False # Simulate game over
        mock_score_manager.get_current_score.return_value = 50
        mock_score_manager.get_high_score.return_value = 100

        game_core = GameCore(0)
        game_core.cobrinha = mock_cobrinha
        game_core.score_manager = mock_score_manager

        result = game_core.update([])

        assert result == "game_over"
        mock_logger.info.assert_any_call("Game Over! Pontuação final: 50. Maior pontuação: 100")

    def test_get_game_state(self, mock_cobrinha, mock_comida, mock_score_manager):
        game_core = GameCore(0)
        game_core.cobrinha = mock_cobrinha
        game_core.comida = mock_comida
        game_core.score_manager = mock_score_manager
        game_core.pausado = True

        game_state = game_core.get_game_state()

        assert game_state["current_score"] == mock_score_manager.get_current_score()
        assert game_state["high_score"] == mock_score_manager.get_high_score()
        assert game_state["comida"] == mock_comida
        assert game_state["cobrinha"] == mock_cobrinha
        assert game_state["pausado"] == True

    def test_get_high_score(self, mock_score_manager):
        mock_score_manager.get_high_score.return_value = 200
        game_core = GameCore(0)
        game_core.score_manager = mock_score_manager
        assert game_core.get_high_score() == 200
