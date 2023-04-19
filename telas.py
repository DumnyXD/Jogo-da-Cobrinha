import pygame
from pygame.locals import *
from cobrinha import Cobrinha
from comida import Comida


def jogo():
    pygame.init()
    fps = pygame.time.Clock()

    largura = 640
    altura = 480

    corFundo = (32, 33, 36)
    corBordas = (42, 43, 46)
    corTitulo = (200, 0, 255)
    corComida = (255, 0, 0)
    corCabeca = (0, 230, 0)
    corCorpo = (0, 255, 0)

    comida = Comida(corComida)
    cobrinha = Cobrinha(corCabeca, corCorpo, (100, 100), )

    fontTitulo = pygame.font.Font("Daydream.ttf", 30)
    titulo = fontTitulo.render("Snake Game", True, corTitulo)

    larguraTitulo, alturaTitulo = fontTitulo.size("Snake Game")

    tituloX = (largura - larguraTitulo) // 2
    tituloy = (50 - alturaTitulo) // 2

    tela = pygame.display.set_mode((largura, altura))

    pygame.display.set_caption("Snake Game")

    while True:
        fps.tick(13)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                if (event.key == K_UP or event.key == K_w) and cobrinha.direcao != "baixo":
                    cobrinha.direcao = "cima"
                    break
                elif (event.key == K_DOWN or event.key == K_s) and cobrinha.direcao != "cima":
                    cobrinha.direcao = "baixo"
                    break
                elif (event.key == K_LEFT or event.key == K_a) and cobrinha.direcao != "direita" and cobrinha.direcao is not None:
                    cobrinha.direcao = "esquerda"
                    break
                elif (event.key == K_RIGHT or event.key == K_d) and cobrinha.direcao != "esquerda":
                    cobrinha.direcao = "direita"
                    break

        if comida.pos == cobrinha.corpo[0]:
            ponto = True
            comida.pos = comida.novaPos()

        else:
            ponto = False

        tela.fill(corFundo)

        cobrinha.move(ponto)

        pygame.draw.rect(tela, corBordas, (5, 45, largura - 10, altura - 50))
        pygame.draw.rect(tela, corFundo, (10, 50, largura - 20, altura - 60))

        tela.blit(titulo, (tituloX, tituloy))

        comida.draw(tela)

        cobrinha.desenha(tela)

        pygame.display.update()
