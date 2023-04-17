import pygame
from pygame.locals import *
from sys import exit
from cobrinha import Cobrinha
from comida import Comida

pygame.init()

fps = pygame.time.Clock()
tamanhoPixel = 10

largura = 640
altura = 480

corFundo = (32, 33, 36)
corBordas = (42, 43, 46)
corTitulo = (255, 255, 255)
corComida = (255, 0, 0)
corCabeca = (0, 230, 0)
corCorpo = (0, 255, 0)

comida = Comida(corComida)
cobrinha = Cobrinha(corCabeca, corCorpo, (100, 100), )  # posição inicial da cobrinha

fontTitulo = pygame.font.Font("Daydream.ttf", 30)
titulo = fontTitulo.render("cobrinha", True, corTitulo)

larguraTitulo, alturaTitulo = fontTitulo.size("cobrinha")

tituloX = (largura - larguraTitulo) // 2
tituloy = (50 - alturaTitulo) // 2

tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption("Cobrinha")

while True:
    fps.tick(13)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_UP and cobrinha.direcao != "baixo":
                cobrinha.direcao = "cima"
            elif event.key == K_DOWN and cobrinha.direcao != "cima":
                cobrinha.direcao = "baixo"
            elif event.key == K_LEFT and cobrinha.direcao != "direita":
                cobrinha.direcao = "esquerda"
            elif event.key == K_RIGHT and cobrinha.direcao != "esquerda":
                cobrinha.direcao = "direita"

    if comida.pos == cobrinha.corpo[0]:
        ponto = True
        comida.pos = comida.novaPos()

    else:
        ponto = False

    tela.fill(corFundo)

    cobrinha.move(ponto)

    pygame.draw.rect(tela, corBordas, (5, 50, largura - 10, altura - 55))
    pygame.draw.rect(tela, corFundo, (10, 55, largura - 20, altura - 65))

    tela.blit(titulo, (tituloX, tituloy))

    comida.draw(tela)

    cobrinha.desenha(tela)

    pygame.display.update()
