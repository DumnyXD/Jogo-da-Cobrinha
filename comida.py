import pygame
import random


class Comida:

    def __init__(self, cor):
        self.cor = cor
        self.pos = self.novaPos()
        # caixaAcao = [15, 65, 615, 415]

    def novaPos(self):
        x = random.randint(20, 610 - 10)
        y = random.randint(70, 450 - 10)
        return (x // 10 * 10, y // 10 * 10)

    def draw(self, tela):
        pygame.draw.rect(tela, self.cor, (self.pos[0], self.pos[1], 10, 10))
