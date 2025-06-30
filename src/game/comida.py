import random
from src.config.game_config import GameConfig
from src.utils.logger import Logger

logger = Logger()


class Comida:
    """
    Classe que representa a comida no jogo Snake.

    Atributos:
    - __cor: Uma tupla que define a cor da comida.
    - __pos: Uma tupla que armazena a posição atual da comida.

    Métodos:
    - NewPos(): Gera uma nova posição aleatória para a comida dentro dos limites da tela.
    - setPos(pos: tuple): Define a posição da comida.
    - getPos(): Retorna a posição atual da comida.
    - getCor(): Retorna a cor da comida.

    """

    def __init__(self):
        self.__cor = (255, 0, 0)  # Definição da cor da comida (vermelho)
        self.__pos = self.NewPos()  # Posição inicial da comida (aleatória)
        logger.info(f"Comida inicializada em {self.__pos}")

    def NewPos(self):
        """Gera uma nova posição aleatória para a comida dentro dos limites da tela."""
        x = random.randrange(10, GameConfig.largura - 20, 10)  # Posição X aleatória (múltiplo de 10)
        y = random.randrange(50, GameConfig.altura - 60, 10)  # Posição Y aleatória (múltiplo de 10)
        logger.info(f"Nova posição da comida gerada: ({x},{y})")
        return (x, y)

    def setPos(self, pos: tuple):
        """Define a posição da comida."""
        self.__pos = pos

    def getPos(self):
        """Retorna a posição atual da comida."""
        return self.__pos

    def getCor(self):
        """Retorna a cor da comida."""
        return self.__cor
