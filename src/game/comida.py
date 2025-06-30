import random
from src.config.game_config import GameConfig
from src.utils.logger import Logger
from src.game.food_position_generator import FoodPositionGenerator
from src.game.position import Position

logger = Logger()


class Comida:
    def __init__(self):
        self.__cor = (255, 0, 0)
        self.__position_generator = FoodPositionGenerator()
        self.__pos = self.__position_generator.generate_new_position()
        logger.info(f"Comida inicializada em {self.__pos}")

    def setPos(self, pos: Position):
        self.__pos = pos

    def getPos(self) -> Position:
        return self.__pos

    def NewPos(self) -> Position:
        return self.__position_generator.generate_new_position()

    def getCor(self):
        return self.__cor
