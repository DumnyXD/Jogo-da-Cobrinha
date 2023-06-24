from sys import exit
from classes import *
from pygame.locals import *


def salvarPontuacao(nome_arquivo, pontuacao):
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(str(pontuacao))


def jogo(maiorPontuacao: int):
    """
    Função que implementa a lógica principal do jogo Snake.

    Argumentos:
    - maiorPontuacao (int): A maior pontuação já alcançada no jogo.

    Retorna:
    - int: A nova maior pontuação alcançada no jogo.
    """

    pygame.init()  # Inicializa o módulo pygame

    pontuacao = 0  # Inicializa a pontuação do jogo como zero

    comida = Comida()  # Cria uma instância da classe Comida
    cobrinha = Cobrinha((100, 100))  # Cria uma instância da classe Cobrinha com posição inicial (100, 100)

    titulo = ObjetoTexto("Snake", Scream.corTitulo, 25, "Daydream.ttf")  # Cria um objeto de texto com o título "Snake"
    titulo.FormatarMeio(25)  # Formata o objeto de texto para ser exibido no centro da tela

    pygame.display.set_caption("Snake Game")  # Define o título da janela do jogo como "Snake Game"

    while True:
        Scream.fps.tick(13)  # Limita o FPS do jogo a 13 (aproximadamente 13 quadros por segundo)

        score = ObjetoTexto(f"score: {pontuacao}", Scream.branco, 17, "Daydream.ttf")  # Cria um objeto de texto com a pontuação atual
        score.FormararSuperiorDireito()  # Formata o objeto de texto para ser exibido no canto superior direito da tela

        record = ObjetoTexto(f"record: {maiorPontuacao}", Scream.branco, 17, "Daydream.ttf")  # Cria um objeto de texto com a maior pontuação alcançada
        record.FormararSuperiorEscerdo()  # Formata o objeto de texto para ser exibido no canto superior esquerdo da tela

        for event in pygame.event.get():
            if event.type == QUIT:  # Se o evento for QUIT (fechar a janela)
                pygame.quit()  # Encerra o pygame
                exit()  # Encerra o programa
            elif event.type == KEYDOWN:  # Se o evento for uma tecla pressionada
                if (event.key == K_UP or event.key == K_w) and cobrinha.getDirecao() != "baixo":  # Se a tecla pressionada for a seta para cima ou a tecla "w" e a direção da cobrinha não for "baixo"
                    cobrinha.setDirecao("cima")  # Define a direção da cobrinha como "cima"
                    break  # Sai do loop
                elif (event.key == K_DOWN or event.key == K_s) and cobrinha.getDirecao() != "cima":  # Se a tecla pressionada for a seta para baixo ou a tecla "s" e a direção da cobrinha não for "cima"
                    cobrinha.setDirecao("baixo")  # Define a direção da cobrinha como "baixo"
                    break  # Sai do loop
                elif (event.key == K_LEFT or event.key == K_a) and cobrinha.getDirecao() != "direita" and cobrinha.getDirecao() is not None:  # Se a tecla pressionada for a seta para a esquerda ou a tecla "a", a direção da cobrinha não for "direita" e a direção da cobrinha não for None
                    cobrinha.setDirecao("esquerda")  # Define a direção da cobrinha como "esquerda"
                    break  # Sai do loop
                elif (event.key == K_RIGHT or event.key == K_d) and cobrinha.getDirecao() != "esquerda":  # Se a tecla pressionada for a seta para a direita ou a tecla "d" e a direção da cobrinha não for "esquerda"
                    cobrinha.setDirecao("direita")  # Define a direção da cobrinha como "direita"
                    break  # Sai do loop

        if comida.getPos() == cobrinha.getPosCabeca():  # Se a posição da comida for igual à posição da cabeça da cobrinha
            ponto = True  # Indica que a cobrinha ganhou um ponto
            pontuacao += 10  # Aumenta a pontuação em 10
            comida.setPos(comida.NewPos())  # Define uma nova posição para a comida
            if maiorPontuacao < pontuacao:  # Se a pontuação atual for maior do que a maior pontuação já alcançada
                maiorPontuacao = pontuacao  # Atualiza a maior pontuação

        else:
            ponto = False  # Indica que a cobrinha não ganhou um ponto

        cobrinha.Move(ponto)  # Move a cobrinha de acordo com a direção e se ganhou ponto ou não

        if not cobrinha.getPerca():  # Se a cobrinha não perdeu o jogo
            return maiorPontuacao  # Retorna a nova maior pontuação alcançada no jogo

        Scream.tela.fill(Scream.corFundo)  # Preenche a tela com a cor de fundo

        pygame.draw.rect(Scream.tela, Scream.corBorda, (5, 45, Scream.largura - 10, Scream.altura - 50))  # Desenha uma borda na tela
        pygame.draw.rect(Scream.tela, Scream.corFundo, (10, 50, Scream.largura - 20, Scream.altura - 60))  # Desenha uma área interna na tela

        titulo.Draw()  # Desenha o objeto de texto do título na tela
        score.Draw()  # Desenha o objeto de texto da pontuação na tela
        record.Draw()  # Desenha o objeto de texto da maior pontuação na tela

        comida.Draw(Scream.tela)  # Desenha a comida na tela

        cobrinha.Draw(Scream.tela)  # Desenha a cobrinha na tela

        pygame.display.update()  # Atualiza a tela do jogo


def menu():
    """
    Função que implementa o menu principal do jogo Snake.

    Retorna:
    - str: A opção selecionada no menu (Iniciar, ou Creditos).

    """
    pygame.init()  # Inicializa o módulo pygame

    titulo1 = ObjetoTexto("Snake", Scream.corTitulo, 60, "Daydream.ttf")  # Cria um objeto de texto com o título "Snake"
    titulo1.FormatarMeio(80)  # Formata o objeto de texto para ser exibido no centro da tela

    titulo2 = ObjetoTexto("Game", Scream.corTitulo, 60, "Daydream.ttf")  # Cria um objeto de texto com a palavra "Game"
    titulo2.FormatarMeio(titulo1.posY + titulo1.altura + 40)  # Formata o objeto de texto para ser exibido abaixo do título "Snake"

    iniciar = ObjetoTexto("Iniciar", Scream.verde, 36, "Daydream.ttf", Scream.corBorda)  # Cria um objeto de texto com a opção "Iniciar"
    iniciar.FormatarMeio(300)  # Formata o objeto de texto para ser exibido na posição vertical 300
    iniciar.CriarBotao()  # Cria um botão com base no objeto de texto

    creditos = ObjetoTexto("Creditos", Scream.verde, 36, "Daydream.ttf", Scream.corBorda)  # Cria um objeto de texto com a opção "Creditos"
    creditos.FormatarMeio(iniciar.posY + 80)  # Formata o objeto de texto para ser exibido abaixo da opção "Iniciar"
    creditos.CriarBotao()  # Cria um botão com base no objeto de texto

    sair = ObjetoTexto("Sair", Scream.vermelho, 36, "Daydream.ttf", Scream.corBorda)  # Cria um objeto de texto com a opção "Sair"
    sair.FormatarMeio(creditos.posY + 80)  # Formata o objeto de texto para ser exibido abaixo da opção "Creditos"
    sair.CriarBotao()  # Cria um botão com base no objeto de texto

    pygame.display.set_caption("Snake Game")  # Define o título da janela do jogo como "Snake Game"

    while True:
        Scream.fps.tick(13)  # Limita o FPS do jogo a 13 (aproximadamente 13 quadros por segundo)

        Scream.tela.fill(Scream.corFundo)  # Preenche a tela com a cor de fundo

        for event in pygame.event.get():
            if event.type == QUIT:  # Se o evento for QUIT (fechar a janela)
                pygame.quit()  # Encerra o pygame
                exit()  # Encerra o programa
            elif event.type == MOUSEBUTTONDOWN:  # Se o evento for um clique do mouse
                if event.button == 1:  # Se o botão pressionado for o botão esquerdo do mouse
                    if iniciar.botao.collidepoint(event.pos):  # Se o clique foi dentro do botão "Iniciar"
                        return "Iniciar"  # Retorna a opção "Iniciar"

                    elif creditos.botao.collidepoint(event.pos):  # Se o clique foi dentro do botão "Creditos"
                        return "Creditos"  # Retorna a opção "Creditos"

                    elif sair.botao.collidepoint(event.pos):  # Se o clique foi dentro do botão "Sair"
                        pygame.quit()  # Encerra o pygame
                        exit()  # Encerra o programa

        titulo1.Draw()  # Desenha o objeto de texto do título "Snake" na tela
        titulo2.Draw()  # Desenha o objeto de texto do título "Game" na tela

        iniciar.Draw()  # Desenha o botão "Iniciar" na tela
        creditos.Draw()  # Desenha o botão "Creditos" na tela
        sair.Draw()  # Desenha o botão "Sair" na tela

        pygame.display.update()  # Atualiza a tela do jogo


def creditos():
    """
    Função que implementa a tela de créditos do jogo Snake.

    Retorna:
    - None

    """
    pygame.init()  # Inicializa o módulo pygame

    volta = False  # Variável que indica se deve voltar ao menu principal

    devs = ObjetoTexto("Dev's:", Scream.verde, 20, "Daydream.ttf")  # Cria um objeto de texto com o título "Dev's"
    devs.FormararSuperiorEscerdo()  # Formata o objeto de texto para ser exibido no canto superior esquerdo da tela

    Wallysson = ObjetoTexto("   Wallysson - RA:323130386", Scream.branco, 20, "Daydream.ttf")  # Cria um objeto de texto com informações do desenvolvedor Wallysson
    Wallysson.FormararSuperiorEscerdo(devs.posY + (devs.altura + 30))  # Formata o objeto de texto para ser exibido abaixo do título "Dev's"

    Fernanda = ObjetoTexto("   Fernanda - RA:323116602", Scream.branco, 20, "Daydream.ttf")  # Cria um objeto de texto com informações do desenvolvedor Fernanda
    Fernanda.FormararSuperiorEscerdo(Wallysson.posY + (Wallysson.altura + 30))  # Formata o objeto de texto para ser exibido abaixo das informações do desenvolvedor Wallysson

    Maysa = ObjetoTexto("   Maysa - RA:323120206", Scream.branco, 20, "Daydream.ttf")  # Cria um objeto de texto com informações do desenvolvedor Maysa
    Maysa.FormararSuperiorEscerdo(Fernanda.posY + (Fernanda.altura + 30))  # Formata o objeto de texto para ser exibido abaixo das informações do desenvolvedor Fernanda

    voltar = ObjetoTexto("Voltar", Scream.branco, 20, "Daydream.ttf", Scream.vermelho)  # Cria um objeto de texto com a opção "Voltar"
    voltar.FormatarInferorDireito()  # Formata o objeto de texto para ser exibido no canto inferior direito da tela
    voltar.CriarBotao()  # Cria um botão com base no objeto de texto

    while True:
        Scream.fps.tick(13)  # Limita o FPS do jogo a 13 (aproximadamente 13 quadros por segundo)

        Scream.tela.fill(Scream.corFundo)  # Preenche a tela com a cor de fundo

        for event in pygame.event.get():
            if event.type == QUIT:  # Se o evento for QUIT (fechar a janela)
                pygame.quit()  # Encerra o pygame
                exit()  # Encerra o programa
            if event.type == MOUSEBUTTONDOWN:  # Se o evento for um clique do mouse
                if event.button == 1:  # Se o botão pressionado for o botão esquerdo do mouse
                    if voltar.botao.collidepoint(event.pos):  # Se o clique foi dentro do botão "Voltar"
                        volta = True

        if volta:
            break  # Sai do loop e retorna ao menu principal

        devs.Draw()  # Desenha o título "Dev's" na tela
        Wallysson.Draw()  # Desenha as informações do desenvolvedor Wallysson na tela
        Maysa.Draw()  # Desenha as informações do desenvolvedor Maysa na tela
        Fernanda.Draw()  # Desenha as informações do desenvolvedor Fernanda na tela

        voltar.Draw()  # Desenha o botão "Voltar" na tela

        pygame.display.update()  # Atualiza a tela do jogo


with open("maior_pontuacao.txt", "r") as f:
    maiorPontuacao = max(int(line.strip()) for line in f)

while True:
    opcao = menu()  # Chama a função menu() para exibir o menu principal e obter a opção escolhida pelo jogador

    if opcao == "Iniciar":  # Se a opção escolhida for "Iniciar"
        maiorPontuacao = jogo(maiorPontuacao)  # Chama a função jogo() passando a maior pontuação atual como argumento e atualiza a maior pontuação
        salvarPontuacao("maior_pontuacao.txt", maiorPontuacao)

    elif opcao == "Creditos":  # Se a opção escolhida for "Creditos"
        creditos()  # Chama a função creditos() para exibir a tela de créditos
