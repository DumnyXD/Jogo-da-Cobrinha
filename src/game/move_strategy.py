from abc import ABC, abstractmethod
from src.game.position import Position

class MoveStrategy(ABC):
    @abstractmethod
    def move(self, current_position: Position) -> Position:
        pass

class MoveUpStrategy(MoveStrategy):
    def move(self, current_position: Position) -> Position:
        return Position(current_position.x, current_position.y - 10)

class MoveDownStrategy(MoveStrategy):
    def move(self, current_position: Position) -> Position:
        return Position(current_position.x, current_position.y + 10)

class MoveLeftStrategy(MoveStrategy):
    def move(self, current_position: Position) -> Position:
        return Position(current_position.x - 10, current_position.y)

class MoveRightStrategy(MoveStrategy):
    def move(self, current_position: Position) -> Position:
        return Position(current_position.x + 10, current_position.y)
