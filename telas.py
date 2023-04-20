import pygame
from sys import exit
from pygame.locals import *
from cobrinha import Cobrinha
from comida import Comida
from tela import tela
import utilidades as ut


def jogo():
    pygame.init()

    corTitulo = (200, 0, 255)
    corComida = (255, 0, 0)
    corCabeca = (0, 230, 0)
    corCorpo = (0, 255, 0)

    comida = Comida(corComida)
    cobrinha = Cobrinha(corCabeca, corCorpo, (100, 100), )

    fontTitulo = pygame.font.Font("Daydream.ttf", 30)
    titulo = fontTitulo.render("Snake Game", True, corTitulo)

    larguraTitulo, alturaTitulo = fontTitulo.size("Snake Game")

    tituloX = (tela.largura - larguraTitulo) // 2
    tituloy = (50 - alturaTitulo) // 2

    pygame.display.set_caption("Snake Game")

    while True:
        tela.fps.tick(13)

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

        tela.tela.fill(tela.corFundo)

        cobrinha.move(ponto)

        pygame.draw.rect(tela.tela, tela.corBorda, (5, 45, tela.largura - 10, tela.altura - 50))
        pygame.draw.rect(tela.tela, tela.corFundo, (10, 50, tela.largura - 20, tela.altura - 60))

        tela.tela.blit(titulo, (tituloX, tituloy))

        comida.draw(tela.tela)

        cobrinha.desenha(tela.tela)

        pygame.display.update()


def menu():
    pygame.init()

    cores = {
        'opcoes':(0, 200, 0),
        'sair':(255, 10, 10),
        'fundoOP':tela.corBorda,
        'fundo':tela.corFundo
    }

    fonteMenu = pygame.font.Font("Daydream.ttf", 36)

    textoIniciar, larguraIniciar, alturaIniciar = ut.CriarTexto("Iniciar", cores['opcoes'], 36, cores['fundoOP'])
    textoCreditos, larguraCreditos, alturaCreditos = ut.CriarTexto("Creditos", cores['opcoes'], 36, cores['fundoOP'])
    textoSair, larguraSair, alturaSair = ut.CriarTexto("Sair", cores['sair'],36,cores['fundoOP'])


    posIniciar = ut.PosTextoMeio((larguraIniciar,alturaIniciar),250)
    posCreditos = ut.PosTextoMeio((larguraCreditos,alturaCreditos),posIniciar[1]+100)

    sairX = (tela.largura - larguraSair) // 2
    sairY = (posCreditos[1] + 100) - (alturaSair // 2)

    botaoIniciar = pygame.Rect(posIniciar[0], posIniciar[1], larguraIniciar, alturaIniciar)
    botaoCredito = pygame.Rect(posCreditos[0], posCreditos[1], larguraCreditos, alturaCreditos)
    botaoSair = pygame.Rect(sairX, sairY, larguraSair, alturaSair)

    pygame.display.set_caption("Snake Game")

    while True:
        tela.fps.tick(13)

        tela.tela.fill(tela.corFundo)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if botaoIniciar.collidepoint(event.pos):
                        return "Iniciar"

                    elif botaoCredito.collidepoint(event.pos):
                        return "Creditos"

                    elif botaoSair.collidepoint(event.pos):
                        pygame.quit()
                        exit()

        tela.tela.blit(textoIniciar, posIniciar)
        tela.tela.blit(textoCreditos, posCreditos)
        tela.tela.blit(textoSair, (sairX, sairY))

        pygame.display.update()


def creditos():
    pygame.init()

    while True:
        tela.fps.tick(13)
        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()
                exit()
