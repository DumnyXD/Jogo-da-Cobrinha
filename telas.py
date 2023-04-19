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

    telaJogo = pygame.display.set_mode((largura, altura))

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
                elif (
                        event.key == K_LEFT or event.key == K_a) and cobrinha.direcao != "direita" and cobrinha.direcao is not None:
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

        telaJogo.fill(corFundo)

        cobrinha.move(ponto)

        pygame.draw.rect(telaJogo, corBordas, (5, 45, largura - 10, altura - 50))
        pygame.draw.rect(telaJogo, corFundo, (10, 50, largura - 20, altura - 60))

        telaJogo.blit(titulo, (tituloX, tituloy))

        comida.draw(telaJogo)

        cobrinha.desenha(telaJogo)

        pygame.display.update()


def menu():
    pygame.init()

    fps = pygame.time.Clock()

    largura = 640
    altura = 480

    telaMenu = pygame.display.set_mode((largura, altura))

    corFundo = (32, 33, 36)
    corBordas = (42, 43, 46)

    fonteMenu = pygame.font.Font("Daydream.ttf", 36)

    textoIniciar = fonteMenu.render("Iniciar", True, (0, 200, 0), corBordas)
    textoCreditos = fonteMenu.render("Creditos", True, (0, 200, 0), corBordas)
    textoSair = fonteMenu.render("Sair", True, (255, 10, 10), corBordas)

    larguraIniciar, alturaIniciar = fonteMenu.size("Iniciar")
    larguraCreditos, alturaCreditos = fonteMenu.size("Creditos")
    larguraSair, alturaSair = fonteMenu.size("Sair")

    iniciarX = (largura - larguraIniciar) // 2
    iniciarY = 250 - (alturaIniciar // 2)

    creditosX = (largura - larguraCreditos) // 2
    creditosY = (iniciarY + 100) - (alturaCreditos // 2)

    sairX = (largura - larguraSair) // 2
    sairY = (creditosY + 100) - (alturaSair // 2)

    pygame.display.set_caption("Snake Game")

    while True:
        fps.tick(13)

        telaMenu.fill(corFundo)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        telaMenu.blit(textoIniciar, (iniciarX, iniciarY))
        telaMenu.blit(textoCreditos, (creditosX, creditosY))
        telaMenu.blit(textoSair, (sairX, sairY))

        pygame.display.update()
