import pygame
import sys


class Cobrinha:
    def __init__(self, corCabeca, corCorpo, posInicial):
        self.corCorpo = corCorpo
        self.corCabeca = corCabeca
        self.tamanho = 10
        self.corpo = [posInicial, (posInicial[0] - 10, posInicial[1]), (posInicial[0] - 20, posInicial[1])]
        self.direcao = None
        self.perca = 1

    def move(self, ponto: bool):
        if self.direcao:
            x, y = self.corpo[0]
            if self.direcao == "cima":
                y -= self.tamanho
            elif self.direcao == "baixo":
                y += self.tamanho
            elif self.direcao == "esquerda":
                x -= self.tamanho
            elif self.direcao == "direita":
                x += self.tamanho

            if x < 10:
                self.perca = 0
            elif x > 620:
                self.perca = 0
            elif y < 50:
                self.perca = 0
            elif y > 460:
                self.perca = 0

            if (x, y) in self.corpo:
                self.perca = 0

            self.corpo.insert(0, (x, y))
            if not ponto:
                self.corpo.pop()

    def desenha(self, tela):
        for pos in self.corpo:
            if pos == self.corpo[0]:
                pygame.draw.rect(tela, self.corCabeca, (pos[0], pos[1], self.tamanho, self.tamanho))

            else:
                pygame.draw.rect(tela, self.corCorpo, (pos[0], pos[1], self.tamanho, self.tamanho))
