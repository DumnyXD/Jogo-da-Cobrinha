import pygame
from tela import Tela


class ObjetoTexto:
    def __init__(self, texto: str, cor: tuple[int, int, int], tamanho: int, fonte: str = None,
                 fundo: tuple[int, int, int] = None):
        self.fonte = fonte
        self.tamanho = tamanho
        self.font = pygame.font.Font(self.fonte, self.tamanho)
        self.texto = texto
        self.cor = cor
        self.fundo = fundo
        self.largura, self.altura = self.font.size(self.texto)
        self.posX = 1
        self.posY = 1
        #self.botao = pygame.Rect(self.posX, self.posY, self.largura, self.altura)
        if self.fundo is None:
            self.render = self.font.render(self.texto, True, self.cor)
        else:
            self.render = self.font.render(self.texto, True, self.cor, self.fundo)

    def Draw(self):
        Tela.tela.blit(self.render, (self.posX, self.posY))

    def FormatarMeio(self, Y: int):
        self.posX = (Tela.largura - self.largura) // 2
        self.posY = Y - (self.altura // 2)
