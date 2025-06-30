import random
from src.config.game_config import GameConfig
from src.utils.logger import Logger
from src.game.position import Position

logger = Logger()

class FoodPositionGenerator:
    def generate_new_position(self) -> Position:
        x = random.randrange(10, GameConfig.largura - 20, 10)
        y = random.randrange(50, GameConfig.altura - 60, 10)
        logger.info(f"Nova posição da comida gerada: ({x},{y})")
        return Position(x, y)