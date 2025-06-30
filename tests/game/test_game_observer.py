import pytest
from abc import ABC, abstractmethod
from src.game.game_observer import GameObserver

class ConcreteGameObserver(GameObserver):
    def update(self, game_state: dict):
        pass

class TestGameObserver:
    def test_game_observer_is_abstract(self):
        assert hasattr(GameObserver, '__abstractmethods__')
        assert 'update' in GameObserver.__abstractmethods__

    def test_concrete_observer_can_be_instantiated(self):
        observer = ConcreteGameObserver()
        assert isinstance(observer, GameObserver)

    def test_concrete_observer_implements_update(self):
        observer = ConcreteGameObserver()
        # This test implicitly checks if update is implemented because ConcreteGameObserver
        # would raise a TypeError if it didn't implement all abstract methods.
        # We can also explicitly check if the method exists and is callable.
        assert hasattr(observer, 'update')
        assert callable(getattr(observer, 'update'))
