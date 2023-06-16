from sys import exit
from classes import *
from pygame.locals import *


def jogo():
    pygame.init()

    comida = Comida()
    cobrinha = Cobrinha((100, 100))

    titulo = ObjetoTexto("Snake Game", Scream.corTitulo, 30, "Daydream.ttf")
    titulo.FormatarMeio(25)

    pygame.display.set_caption("Snake Game")

    while True:
        Scream.fps.tick(13)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                if (event.key == K_UP or event.key == K_w) and cobrinha.getDirecao() != "baixo":
                    cobrinha.setDirecao("cima")
                    break
                elif (event.key == K_DOWN or event.key == K_s) and cobrinha.getDirecao() != "cima":
                    cobrinha.setDirecao("baixo")
                    break
                elif (
                        event.key == K_LEFT or event.key == K_a) and cobrinha.getDirecao() != "direita" and cobrinha.getDirecao() is not None:
                    cobrinha.setDirecao("esquerda")
                    break
                elif (event.key == K_RIGHT or event.key == K_d) and cobrinha.getDirecao() != "esquerda":
                    cobrinha.setDirecao("direita")
                    break

        if comida.getPos() == cobrinha.getPosCabeca():
            ponto = True
            comida.setPos(comida.NewPos())

        else:
            ponto = False

        cobrinha.Move(ponto)

        if not cobrinha.getPerca():
            break

        Scream.tela.fill(Scream.corFundo)

        pygame.draw.rect(Scream.tela, Scream.corBorda, (5, 45, Scream.largura - 10, Scream.altura - 50))
        pygame.draw.rect(Scream.tela, Scream.corFundo, (10, 50, Scream.largura - 20, Scream.altura - 60))

        titulo.Draw()

        comida.Draw(Scream.tela)

        cobrinha.Draw(Scream.tela)

        pygame.display.update()


def menu():
    pygame.init()

    iniciar = ObjetoTexto("Iniciar", Scream.verde, 36, "Daydream.ttf", Scream.corBorda)
    iniciar.FormatarMeio(250)
    iniciar.CriarBotao()

    creditos = ObjetoTexto("Creditos", Scream.verde, 36, "Daydream.ttf", Scream.corBorda)
    creditos.FormatarMeio(iniciar.posY + 100)
    creditos.CriarBotao()

    sair = ObjetoTexto("Sair", Scream.vermelho, 36, "Daydream.ttf", Scream.corBorda)
    sair.FormatarMeio(creditos.posY + 100)
    sair.CriarBotao()

    pygame.display.set_caption("Snake Game")

    while True:
        Scream.fps.tick(13)

        Scream.tela.fill(Scream.corFundo)

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

                    elif sair.botao.collidepoint(event.pos):
                        pygame.quit()
                        exit()

        iniciar.Draw()
        creditos.Draw()
        sair.Draw()

        pygame.display.update()


def creditos():
    pygame.init()

    volta = False

    nomeWallysson = ObjetoTexto("Wallysson - 323130386", Scream.branco, 20, "Daydream.ttf")

    voltar = ObjetoTexto("Voltar", Scream.branco, 20, "Daydream.ttf", Scream.vermelho)
    voltar.FormatarInferorDireito()
    voltar.CriarBotao()

    while True:
        Scream.fps.tick(13)
        Scream.tela.fill(Scream.corFundo)
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


while True:
    opcao = menu()
    if opcao == "Iniciar":
        jogo()

    elif opcao == "Creditos":
        creditos()
