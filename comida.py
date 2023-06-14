import pygame
import random


class Comida:

    def __init__(self, cor):
        self.__cor = cor
        self.__pos = self.NewPos()

    def setPos(self, pos: tuple[int, int]):
        self.__pos = pos
    def getPos(self):
        return self.__pos

    def NewPos(self):
        x = random.randint(10, 620 - 10)
        y = random.randint(50, 460 - 10)
        return x // 10 * 10, y // 10 * 10

    def Draw(self, tela):
        pygame.draw.rect(tela, self.__cor, (self.__pos[0], self.__pos[1], 10, 10))
