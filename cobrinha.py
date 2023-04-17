import pygame
import sys


class Cobrinha:
    def __init__(self, corCabeca, corCorpo, posInicial):
        self.corCorpo = corCorpo
        self.corCabeca = corCabeca
        self.tamanho = 10
        self.corpo = [posInicial, (posInicial[0] - 10, posInicial[1]), (posInicial[0] - 20, posInicial[1])]
        self.direcao = None

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

            # Verifica se a cabeça da cobra está fora da área de ação
            if x < 20:
                x = 610
            elif x > 610:
                x = 20
            elif y < 70:
                y = 480
            elif y > 480:
                y = 70

            if (x, y) in self.corpo:
                pygame.quit()
                sys.exit()

            self.corpo.insert(0, (x, y))
            if not ponto:
                self.corpo.pop()

    def desenha(self, tela):
        for pos in self.corpo:
            if pos == self.corpo[0]:
                pygame.draw.rect(tela, self.corCabeca, (pos[0], pos[1], self.tamanho, self.tamanho))

            else:
                pygame.draw.rect(tela, self.corCorpo, (pos[0], pos[1], self.tamanho, self.tamanho))
