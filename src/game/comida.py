import random
import pygame
from src.utils.logger import Logger

logger = Logger()


class Comida:
    """
    Classe que representa a comida do jogo Snake.

    Atributos:
    - __cor: Uma tupla que define a cor da comida.
    - __pos: Uma tupla que armazena a posição da comida.

    Métodos:
    - setPos(pos: tuple[int, int]): Define a posição da comida.
    - getPos(): Retorna a posição da comida.
    - NewPos(): Gera uma nova posição aleatória para a comida.
    - Draw(tela): Desenha a comida na tela especificada.

    """

    def __init__(self):
        self.__cor = (255, 0, 0)  # Definição da cor da comida
        self.__pos = self.NewPos()  # Geração de uma posição inicial para a comida
        logger.info(f"Comida inicializada em {self.__pos}")

    def setPos(self, pos: tuple[int, int]):
        """Define a posição da comida."""
        self.__pos = pos

    def getPos(self):
        """Retorna a posição da comida."""
        return self.__pos

    def NewPos(self):
        """
        Gera uma nova posição aleatória para a comida.

        A nova posição é gerada dentro dos limites da tela, considerando o tamanho da comida.

        """
        x = random.randint(10, 620 - 10)
        y = random.randint(50, 460 - 10)
        new_pos = x // 10 * 10, y // 10 * 10
        logger.info(f"Gerando nova posição para a comida: {new_pos}")
        return new_pos

    def Draw(self, tela):
        """Desenha a comida na tela especificada."""
        pygame.draw.rect(tela, self.__cor, (self.__pos[0], self.__pos[1], 10, 10))