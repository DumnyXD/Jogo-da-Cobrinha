import pytest
from src.config.game_config import GameConfig

class TestGameConfig:
    def test_largura(self):
        assert GameConfig.largura == 640

    def test_altura(self):
        assert GameConfig.altura == 480

    def test_fps(self):
        assert GameConfig.FPS == 13

    def test_cor_fundo(self):
        assert GameConfig.corFundo == (0, 0, 0)

    def test_cor_borda(self):
        assert GameConfig.corBorda == (64, 64, 64)

    def test_cor_titulo(self):
        assert GameConfig.corTitulo == (0, 255, 0)

    def test_branco(self):
        assert GameConfig.branco == (255, 255, 255)

    def test_verde(self):
        assert GameConfig.verde == (0, 255, 0)

    def test_vermelho(self):
        assert GameConfig.vermelho == (255, 0, 0)
