from sys import exit
import pygame
from pygame.locals import *

from src.game.game_core import GameCore
from src.graphics.pygame_renderer import PygameRenderer
from src.config.game_config import GameConfig
from src.graphics.objeto_texto import ObjetoTexto


def salvarPontuacao(nome_arquivo, pontuacao):
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(str(pontuacao))


def jogo(maiorPontuacao: int):
    
    renderer = PygameRenderer()
    game_core = GameCore(maiorPontuacao)

    while True:
        events = pygame.event.get()
        actions = []
        for event in events:
            if event.type == QUIT:
                renderer.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    actions.append("toggle_pause")
                if (event.key == pygame.K_UP or event.key == pygame.K_w):
                    actions.append("move_up")
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                    actions.append("move_down")
                elif (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                    actions.append("move_left")
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                    actions.append("move_right")

        game_state = game_core.update(actions)

        if game_state == "game_over":
            return game_core.maiorPontuacao

        renderer.render(game_core.get_game_state())
        renderer.tick()


def menu(renderer: PygameRenderer):
    titulo1 = ObjetoTexto("Snake", GameConfig.corTitulo, 60, "Daydream.ttf")
    titulo1.FormatarMeio(80)

    titulo2 = ObjetoTexto("Game", GameConfig.corTitulo, 60, "Daydream.ttf")
    titulo2.FormatarMeio(titulo1.posY + titulo1.altura + 40)

    iniciar = ObjetoTexto("Iniciar", GameConfig.verde, 36, "Daydream.ttf")
    iniciar.FormatarMeio(300)
    iniciar.CriarBotao()

    creditos = ObjetoTexto("Creditos", GameConfig.verde, 36, "Daydream.ttf")
    creditos.FormatarMeio(iniciar.posY + 80)
    creditos.CriarBotao()

    sair = ObjetoTexto("Sair", GameConfig.vermelho, 36, "Daydream.ttf")
    sair.FormatarMeio(creditos.posY + 80)
    sair.CriarBotao()

    while True:
        renderer.tick()
        renderer.screen.fill(GameConfig.corFundo)

        for event in pygame.event.get():
            if event.type == QUIT:
                renderer.quit()
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if iniciar.botao.collidepoint(event.pos):
                        return "Iniciar"

                    elif creditos.botao.collidepoint(event.pos):
                        return "Creditos"

                    elif sair.botao.collidepoint(event.pos):
                        renderer.quit()
                        exit()

        titulo1.Draw(renderer.screen)
        titulo2.Draw(renderer.screen)

        iniciar.Draw(renderer.screen)
        creditos.Draw(renderer.screen)
        sair.Draw(renderer.screen)

        pygame.display.update()


def creditos(renderer: PygameRenderer):
    volta = False

    devs = ObjetoTexto("Dev's:", GameConfig.verde, 20, "Daydream.ttf")
    devs.FormararSuperiorEscerdo()

    Wallysson = ObjetoTexto("   Wallysson - RA:323130386", GameConfig.branco, 20, "Daydream.ttf")
    Wallysson.FormararSuperiorEscerdo(devs.posY + (devs.altura + 30))

    Fernanda = ObjetoTexto("   Fernanda - RA:323116602", GameConfig.branco, 20, "Daydream.ttf")
    Fernanda.FormararSuperiorEscerdo(Wallysson.posY + (Wallysson.altura + 30))

    Maysa = ObjetoTexto("   Maysa - RA:323120206", GameConfig.branco, 20, "Daydream.ttf")
    Maysa.FormararSuperiorEscerdo(Fernanda.posY + (Fernanda.altura + 30))

    voltar = ObjetoTexto("Voltar", GameConfig.branco, 20, "Daydream.ttf", GameConfig.vermelho)
    voltar.FormatarInferorDireito()
    voltar.CriarBotao()

    while True:
        renderer.tick()
        renderer.screen.fill(GameConfig.corFundo)

        for event in pygame.event.get():
            if event.type == QUIT:
                renderer.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if voltar.botao.collidepoint(event.pos):
                        volta = True

        if volta:
            break

        devs.Draw(renderer.screen)
        Wallysson.Draw(renderer.screen)
        Maysa.Draw(renderer.screen)
        Fernanda.Draw(renderer.screen)

        voltar.Draw(renderer.screen)

        pygame.display.update()


with open("maior_pontuacao.txt", "r") as f:
    maiorPontuacao = max(int(line.strip()) for line in f)

renderer = PygameRenderer()

while True:
    opcao = menu(renderer)

    if opcao == "Iniciar":
        maiorPontuacao = jogo(maiorPontuacao)
        salvarPontuacao("maior_pontuacao.txt", maiorPontuacao)

    elif opcao == "Creditos":
        creditos(renderer)