from abc import ABC, abstractmethod

class GameObserver(ABC):
    @abstractmethod
    def update(self, game_state: dict):
        pass
