import pygame


class Tela:
    corFundo = (32, 33, 36)
    corBorda = (42, 43, 46)
    largura = 640
    altura = 480
    fps = pygame.time.Clock()
    tela = pygame.display.set_mode((largura, altura))
