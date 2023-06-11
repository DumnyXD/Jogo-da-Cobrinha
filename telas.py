import pygame
from sys import exit
from pygame.locals import *
from cobrinha import Cobrinha
from comida import Comida
from tela import Tela
from texto import ObjetoTexto
import utilidades as ut


def jogo():
    pygame.init()

    corTitulo = (200, 0, 255)
    corComida = (255, 0, 0)
    corCabeca = (0, 230, 0)
    corCorpo = (0, 255, 0)

    comida = Comida(corComida)
    cobrinha = Cobrinha(corCabeca, corCorpo, (100, 100))

    titulo = ObjetoTexto("Snake Game", corTitulo, 30, "Daydream.ttf")

    fontTitulo = pygame.font.Font("Daydream.ttf", 30)
    titulo = fontTitulo.render("Snake Game", True, corTitulo)

    larguraTitulo, alturaTitulo = fontTitulo.size("Snake Game")

    tituloX = (Tela.largura - larguraTitulo) // 2
    tituloy = (50 - alturaTitulo) // 2

    pygame.display.set_caption("Snake Game")

    while True:
        Tela.fps.tick(13)

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

        if cobrinha.perca == 0:
            break

        if comida.pos == cobrinha.corpo[0]:
            ponto = True
            comida.pos = comida.novaPos()

        else:
            ponto = False

        Tela.tela.fill(Tela.corFundo)

        cobrinha.move(ponto)

        pygame.draw.rect(Tela.tela, Tela.corBorda, (5, 45, Tela.largura - 10, Tela.altura - 50))
        pygame.draw.rect(Tela.tela, Tela.corFundo, (10, 50, Tela.largura - 20, Tela.altura - 60))

        Tela.tela.blit(titulo, (tituloX, tituloy))

        comida.draw(Tela.tela)

        cobrinha.desenha(Tela.tela)

        pygame.display.update()


def menu():
    pygame.init()

    cores = {
        'opcoes': (0, 200, 0),
        'sair': (255, 10, 10),
        'fundoOP': Tela.corBorda,
        'fundo': Tela.corFundo
    }

    iniciar = ObjetoTexto("Iniciar", cores['opcoes'], 36, "Daydream.ttf", cores['fundoOP'])
    iniciar.FormatarMeio(250)
    iniciar.CriarBotao()

    creditos = ObjetoTexto("Creditos", cores['opcoes'], 36, "Daydream.ttf", cores['fundoOP'])
    creditos.FormatarMeio(iniciar.posY + 100)
    creditos.CriarBotao()

    textoSair, larguraSair, alturaSair = ut.CriarTexto("Sair", cores['sair'], 36, cores['fundoOP'])

    sairX = (Tela.largura - larguraSair) // 2
    sairY = (creditos.posY + 100) - (alturaSair // 2)

    botaoSair = pygame.Rect(sairX, sairY, larguraSair, alturaSair)

    pygame.display.set_caption("Snake Game")

    while True:
        Tela.fps.tick(13)

        Tela.tela.fill(Tela.corFundo)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if iniciar.botao.collidepoint(event.pos):
                        return "Iniciar"

                    elif creditos.botao.collidepoint(event.pos):
                        return "Creditos"

                    elif botaoSair.collidepoint(event.pos):
                        pygame.quit()
                        exit()

        iniciar.Draw()
        creditos.Draw()
        Tela.tela.blit(textoSair, (sairX, sairY))

        pygame.display.update()


def creditos():
    pygame.init()

    volta = False

    voltar = ObjetoTexto("Voltar", (255, 255, 255), 20, "Daydream.ttf", (255, 10, 10))
    voltar.FormatarInferorDireito()
    voltar.CriarBotao()

    while True:
        Tela.fps.tick(13)
        Tela.tela.fill(Tela.corFundo)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if voltar.botao.collidepoint(event.pos):
                        volta = True

        if volta:
            break

        voltar.Draw()

        pygame.display.update()
