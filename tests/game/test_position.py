import pytest
from src.game.position import Position

class TestPosition:
    def test_position_creation(self):
        pos = Position(10, 20)
        assert pos.x == 10
        assert pos.y == 20

    def test_position_equality(self):
        pos1 = Position(5, 10)
        pos2 = Position(5, 10)
        pos3 = Position(10, 5)
        assert pos1 == pos2
        assert pos1 != pos3

    def test_position_hash(self):
        pos1 = Position(1, 2)
        pos2 = Position(1, 2)
        pos3 = Position(2, 1)
        assert hash(pos1) == hash(pos2)
        assert hash(pos1) != hash(pos3)

    def test_position_repr(self):
        pos = Position(30, 40)
        assert repr(pos) == "Position(x=30, y=40)"

    def test_position_inequality_with_non_position_object(self):
        pos = Position(1, 1)
        assert pos != (1, 1)
        assert pos != "not a position"
