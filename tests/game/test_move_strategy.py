import pytest
from src.game.move_strategy import MoveUpStrategy, MoveDownStrategy, MoveLeftStrategy, MoveRightStrategy
from src.game.position import Position

class TestMoveStrategies:
    def test_move_up_strategy(self):
        strategy = MoveUpStrategy()
        current_pos = Position(100, 100)
        new_pos = strategy.move(current_pos)
        assert new_pos == Position(100, 90)

    def test_move_down_strategy(self):
        strategy = MoveDownStrategy()
        current_pos = Position(100, 100)
        new_pos = strategy.move(current_pos)
        assert new_pos == Position(100, 110)

    def test_move_left_strategy(self):
        strategy = MoveLeftStrategy()
        current_pos = Position(100, 100)
        new_pos = strategy.move(current_pos)
        assert new_pos == Position(90, 100)

    def test_move_right_strategy(self):
        strategy = MoveRightStrategy()
        current_pos = Position(100, 100)
        new_pos = strategy.move(current_pos)
        assert new_pos == Position(110, 100)
