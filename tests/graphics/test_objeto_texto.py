import pytest
from unittest.mock import MagicMock, patch
from src.graphics.objeto_texto import ObjetoTexto
from src.config.game_config import GameConfig

# Mock Pygame
@pytest.fixture(autouse=True)
def mock_pygame():
    with patch('pygame.font.init'), \
         patch('pygame.font.Font') as mock_font_class, \
         patch('pygame.Rect') as mock_rect_class, \
         patch('pygame.display.set_mode'):

        # Configure mock_font_class to return a mock font instance
        mock_font_instance = MagicMock()
        mock_font_instance.size.return_value = (100, 20) # Default size for text
        mock_font_instance.render.return_value = MagicMock() # Mock rendered surface
        mock_font_class.return_value = mock_font_instance

        # Configure mock_rect_class to return a mock Rect instance
        mock_rect_instance = MagicMock()
        mock_rect_class.return_value = mock_rect_instance

        yield

# Mocking the Logger to prevent file operations during tests
@pytest.fixture(autouse=True)
def mock_logger():
    with patch('src.graphics.objeto_texto.logger') as mock_log:
        yield mock_log

class TestObjetoTexto:
    def test_objeto_texto_initialization_no_background(self):
        text_obj = ObjetoTexto("Hello", (255, 255, 255), 20, "Daydream.ttf")
        assert text_obj.texto == "Hello"
        assert text_obj.cor == (255, 255, 255)
        assert text_obj.tamanho == 20
        assert text_obj.fonte == "Daydream.ttf"
        assert text_obj.fundo is None
        assert text_obj.largura == 100
        assert text_obj.altura == 20
        assert text_obj.posX == 1
        assert text_obj.posY == 1
        assert text_obj.botao is None
        assert text_obj.render is not None
        text_obj.font.render.assert_called_with("Hello", True, (255, 255, 255))

    def test_objeto_texto_initialization_with_background(self):
        text_obj = ObjetoTexto("World", (0, 0, 0), 30, "Daydream.ttf", (100, 100, 100))
        assert text_obj.texto == "World"
        assert text_obj.cor == (0, 0, 0)
        assert text_obj.tamanho == 30
        assert text_obj.fonte == "Daydream.ttf"
        assert text_obj.fundo == (100, 100, 100)
        text_obj.font.render.assert_called_with("World", True, (0, 0, 0), (100, 100, 100))

    def test_draw(self):
        text_obj = ObjetoTexto("Test", (255, 0, 0), 15, "Daydream.ttf")
        mock_screen = MagicMock()
        text_obj.Draw(mock_screen)
        mock_screen.blit.assert_called_with(text_obj.render, (text_obj.posX, text_obj.posY))

    def test_formatar_meio(self):
        text_obj = ObjetoTexto("Center", (0, 255, 0), 25, "Daydream.ttf")
        text_obj.largura = 200 # Mock a specific width for calculation
        text_obj.altura = 30 # Mock a specific height for calculation
        y_pos = 240
        text_obj.FormatarMeio(y_pos)
        expected_pos_x = (GameConfig.largura - 200) // 2
        expected_pos_y = y_pos - (30 // 2)
        assert text_obj.posX == expected_pos_x
        assert text_obj.posY == expected_pos_y

    def test_formatar_inferior_direito(self):
        text_obj = ObjetoTexto("BottomRight", (0, 0, 255), 18, "Daydream.ttf")
        text_obj.largura = 150
        text_obj.altura = 25
        text_obj.FormatarInferorDireito()
        expected_pos_x = (GameConfig.largura - 150) - 10
        expected_pos_y = (GameConfig.altura - 25) - 10
        assert text_obj.posX == expected_pos_x
        assert text_obj.posY == expected_pos_y

    def test_criar_botao(self):
        text_obj = ObjetoTexto("Button", (255, 255, 0), 22, "Daydream.ttf")
        text_obj.posX = 50
        text_obj.posY = 60
        text_obj.largura = 120
        text_obj.altura = 35
        text_obj.CriarBotao()
        assert text_obj.botao is not None
        # Verify that pygame.Rect was called with the correct arguments
        from pygame import Rect # Import Rect directly for assertion
        Rect.assert_called_with(50, 60, 120, 35)

    def test_formarar_superior_direito(self):
        text_obj = ObjetoTexto("TopRight", (255, 0, 255), 20, "Daydream.ttf")
        text_obj.largura = 100
        text_obj.altura = 20
        text_obj.FormararSuperiorDireito()
        expected_pos_x = (GameConfig.largura - 100) - 10
        expected_pos_y = 25 - (20 // 2)
        assert text_obj.posX == expected_pos_x
        assert text_obj.posY == expected_pos_y

    def test_formarar_superior_esquerdo_no_y(self):
        text_obj = ObjetoTexto("TopLeft", (0, 255, 255), 20, "Daydream.ttf")
        text_obj.largura = 100
        text_obj.altura = 20
        text_obj.FormararSuperiorEscerdo()
        expected_pos_x = 10
        expected_pos_y = 25 - (20 // 2)
        assert text_obj.posX == expected_pos_x
        assert text_obj.posY == expected_pos_y

    def test_formarar_superior_esquerdo_with_y(self):
        text_obj = ObjetoTexto("TopLeftY", (123, 45, 67), 20, "Daydream.ttf")
        text_obj.largura = 100
        text_obj.altura = 20
        y_pos = 50
        text_obj.FormararSuperiorEscerdo(y_pos)
        expected_pos_x = 10
        expected_pos_y = y_pos - (20 // 2)
        assert text_obj.posX == expected_pos_x
        assert text_obj.posY == expected_pos_y
