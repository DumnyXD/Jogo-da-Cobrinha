import pytest
import pygame
from unittest.mock import MagicMock, patch
from src.graphics.pygame_renderer import PygameRenderer
from src.config.game_config import GameConfig
from src.game.position import Position

# Mock Pygame
@pytest.fixture(autouse=True)
def mock_pygame():
    with patch('pygame.init'), \
         patch('pygame.display.set_mode') as mock_set_mode, \
         patch('pygame.display.set_caption'), \
         patch('pygame.time.Clock') as mock_clock_class, \
         patch('pygame.draw.rect'), \
         patch('pygame.display.update'), \
         patch('pygame.quit'):

        mock_screen = MagicMock() # Mock the screen surface
        mock_set_mode.return_value = mock_screen

        mock_clock_instance = MagicMock()
        mock_clock_class.return_value = mock_clock_instance

        yield

# Mocking the Logger to prevent file operations during tests
@pytest.fixture(autouse=True)
def mock_logger():
    with patch('src.graphics.pygame_renderer.logger') as mock_log:
        yield mock_log

# Mock ObjetoTexto
@pytest.fixture
def mock_objeto_texto_class():
    with patch('src.graphics.pygame_renderer.ObjetoTexto') as mock:
        yield mock

class TestPygameRenderer:
    def test_initialization(self):
        renderer = PygameRenderer()
        assert pygame.init.called_once()
        assert pygame.display.set_mode.called_once_with((GameConfig.largura, GameConfig.altura))
        assert pygame.display.set_caption.called_once_with("Snake Game")
        assert pygame.time.Clock.called_once()

    def test_update_calls_render(self):
        renderer = PygameRenderer()
        renderer.render = MagicMock() # Mock the render method
        game_state = {"some": "state"}
        renderer.update(game_state)
        renderer.render.assert_called_once_with(game_state)

    def test_render_elements(self, mock_objeto_texto_class):
        renderer = PygameRenderer()
        mock_screen = renderer.screen # Get the mocked screen

        # Mock game_state components
        mock_comida = MagicMock()
        mock_comida.getCor.return_value = (255, 0, 0)
        mock_comida.getPos.return_value = Position(100, 100)

        mock_cobrinha = MagicMock()
        mock_cobrinha.getCorpo.return_value = [Position(50, 50), Position(60, 50)]
        mock_cobrinha.getPosCabeca.return_value = Position(50, 50)
        mock_cobrinha.getCorCabeca.return_value = (0, 255, 0)
        mock_cobrinha.getCorCorpo.return_value = (0, 200, 0)

        game_state = {
            "current_score": 10,
            "high_score": 50,
            "comida": mock_comida,
            "cobrinha": mock_cobrinha,
            "pausado": False,
        }

        renderer.render(game_state)

        # Assert screen fill and rect draws
        mock_screen.fill.assert_called_once_with(GameConfig.corFundo)
        pygame.draw.rect.assert_any_call(mock_screen, GameConfig.corBorda, (5, 45, GameConfig.largura - 10, GameConfig.altura - 50))
        pygame.draw.rect.assert_any_call(mock_screen, GameConfig.corFundo, (10, 50, GameConfig.largura - 20, GameConfig.altura - 60))

        # Assert ObjetoTexto calls
        assert mock_objeto_texto_class.call_count == 3 # Title, score, record
        mock_objeto_texto_class.return_value.FormatarMeio.assert_called_with(25)
        mock_objeto_texto_class.return_value.FormararSuperiorDireito.assert_called_once()
        mock_objeto_texto_class.return_value.FormararSuperiorEscerdo.assert_called_once()
        assert mock_objeto_texto_class.return_value.Draw.call_count == 3

        # Assert food and snake draws
        pygame.draw.rect.assert_any_call(mock_screen, (255, 0, 0), (100, 100, 10, 10)) # Food
        pygame.draw.rect.assert_any_call(mock_screen, (0, 255, 0), (50, 50, 10, 10)) # Snake head
        pygame.draw.rect.assert_any_call(mock_screen, (0, 200, 0), (60, 50, 10, 10)) # Snake body

        pygame.display.update.assert_called_once()

    def test_render_paused_state(self, mock_objeto_texto_class):
        renderer = PygameRenderer()
        mock_screen = renderer.screen

        game_state = {
            "current_score": 0,
            "high_score": 0,
            "comida": MagicMock(),
            "cobrinha": MagicMock(),
            "pausado": True,
        }

        renderer.render(game_state)

        mock_objeto_texto_class.assert_any_call("PAUSADO", GameConfig.branco, 40, "Daydream.ttf")
        assert mock_objeto_texto_class.return_value.FormatarMeio.call_count == 2
        assert mock_objeto_texto_class.return_value.Draw.call_count == 4

    def test_tick(self):
        renderer = PygameRenderer()
        renderer.tick()
        renderer.clock.tick.assert_called_once_with(GameConfig.FPS)

    def test_quit(self):
        renderer = PygameRenderer()
        renderer.quit()
        pygame.quit.assert_called_once()
