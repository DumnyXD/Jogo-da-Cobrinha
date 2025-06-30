import pytest
from unittest.mock import MagicMock, patch
from src.game.cobrinha import Cobrinha
from src.game.position import Position
from src.config.game_config import GameConfig

# Mocking the Logger to prevent file operations during tests


class TestCobrinha:
    def test_cobrinha_initialization(self):
        initial_pos = Position(100, 100)
        cobrinha = Cobrinha(initial_pos)
        assert cobrinha.getPosCabeca() == initial_pos
        assert len(cobrinha.getCorpo()) == 1
        assert cobrinha.getPerca() is True
        assert cobrinha.getDirecao() is None
        assert cobrinha.getCorCabeca() == (0, 230, 0)
        assert cobrinha.getCorCorpo() == (0, 255, 0)

    def test_set_get_perca(self):
        cobrinha = Cobrinha(Position(100, 100))
        cobrinha.setPerca(False)
        assert cobrinha.getPerca() is False
        cobrinha.setPerca(True)
        assert cobrinha.getPerca() is True

    def test_get_pos_cabeca(self):
        initial_pos = Position(100, 100)
        cobrinha = Cobrinha(initial_pos)
        assert cobrinha.getPosCabeca() == initial_pos

    def test_set_direcao_valid_changes(self):
        cobrinha = Cobrinha(Position(100, 100))
        cobrinha.setDirecao("cima")
        assert cobrinha.getDirecao() == "cima"
        cobrinha.setDirecao("direita")
        assert cobrinha.getDirecao() == "direita"

    def test_set_direcao_invalid_changes(self):
        cobrinha = Cobrinha(Position(100, 100))
        cobrinha.setDirecao("cima")
        cobrinha.setDirecao("baixo")  # Invalid change
        assert cobrinha.getDirecao() == "cima"

        cobrinha.setDirecao("direita")
        cobrinha.setDirecao("esquerda") # Invalid change
        assert cobrinha.getDirecao() == "direita"

    def test_move_no_direction(self):
        cobrinha = Cobrinha(Position(100, 100))
        initial_body = list(cobrinha.getCorpo())
        cobrinha.Move(False)
        assert cobrinha.getCorpo() == initial_body

    @pytest.mark.parametrize("direction, expected_head_pos", [
        ("cima", Position(100, 90)),
        ("baixo", Position(100, 110)),
        ("esquerda", Position(90, 100)),
        ("direita", Position(110, 100)),
    ])
    def test_move_without_point(self, direction, expected_head_pos):
        cobrinha = Cobrinha(Position(100, 100))
        cobrinha.setDirecao(direction)
        initial_tail = cobrinha.getCorpo()[-1]
        cobrinha.Move(False)
        assert cobrinha.getPosCabeca() == expected_head_pos
        assert len(cobrinha.getCorpo()) == 1  # Length remains same
        assert initial_tail not in cobrinha.getCorpo() # Tail should be popped

    @pytest.mark.parametrize("direction, expected_head_pos", [
        ("cima", Position(100, 90)),
        ("baixo", Position(100, 110)),
        ("esquerda", Position(90, 100)),
        ("direita", Position(110, 100)),
    ])
    def test_move_with_point(self, direction, expected_head_pos):
        cobrinha = Cobrinha(Position(100, 100))
        cobrinha.setDirecao(direction)
        initial_tail = cobrinha.getCorpo()[-1]
        cobrinha.Move(True)
        assert cobrinha.getPosCabeca() == expected_head_pos
        assert len(cobrinha.getCorpo()) == 2  # Length increases
        assert initial_tail in cobrinha.getCorpo() # Tail should not be popped

    @pytest.mark.parametrize("x, y", [
        (5, 100),  # Left wall
        (GameConfig.largura - 15, 100), # Right wall
        (100, 45), # Top wall
        (100, GameConfig.altura - 15) # Bottom wall
    ])
    def test_collision_with_walls(self, x, y):
        cobrinha = Cobrinha(Position(100, 100))
        # Directly call _check_collision for testing boundary conditions
        assert cobrinha._check_collision(x, y, False) is True

    def test_no_collision_with_walls(self):
        cobrinha = Cobrinha(Position(100, 100))
        assert cobrinha._check_collision(150, 150, False) is False

    def test_collision_with_self(self):
        cobrinha = Cobrinha(Position(100, 100))
        # Manually create a scenario where head collides with body
        cobrinha._Cobrinha__corpo = [Position(100, 100), Position(100, 110), Position(100, 120)]
        assert cobrinha._check_collision(100, 110, False) is True
        assert cobrinha._check_collision(100, 100, False) is False # Head position should not cause collision

    def test_move_collision_sets_perca_false(self):
        cobrinha = Cobrinha(Position(100, 100))
        cobrinha.setDirecao("cima")
        # Force a collision by setting head near wall
        cobrinha._Cobrinha__corpo[0] = Position(100, 50) # Just outside top boundary
        cobrinha.Move(False)
        assert cobrinha.getPerca() is False

    def test_get_corpo(self):
        initial_pos = Position(100, 100)
        cobrinha = Cobrinha(initial_pos)
        body = cobrinha.getCorpo()
        assert isinstance(body, list)
        assert len(body) == 1
        assert body[0] == initial_pos

    def test_get_cor_cabeca(self):
        cobrinha = Cobrinha(Position(100, 100))
        assert cobrinha.getCorCabeca() == (0, 230, 0)

    def test_get_cor_corpo(self):
        cobrinha = Cobrinha(Position(100, 100))
        assert cobrinha.getCorCorpo() == (0, 255, 0)
