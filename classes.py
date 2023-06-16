import random
import pygame


class Scream:
    """
    Classe que define algumas constantes de cores e configurações de tela para o jogo Snake.

    Atributos:
    - verde: Uma tupla que representa a cor verde.
    - branco: Uma tupla que representa a cor branca.
    - vermelho: Uma tupla que representa a cor vermelha.
    - corFundo: Uma tupla que representa a cor de fundo da tela.
    - corBorda: Uma tupla que representa a cor da borda da tela.
    - corTitulo: Uma tupla que representa a cor do título do jogo.
    - largura: Um inteiro que define a largura da tela do jogo.
    - altura: Um inteiro que define a altura da tela do jogo.
    - fps: Um objeto Clock do módulo pygame para controlar a taxa de quadros por segundo.
    - tela: Um objeto Surface do módulo pygame que representa a janela do jogo.

    """

    verde = (10, 255, 10)  # Definição da cor verde
    branco = (255, 255, 255)  # Definição da cor branca
    vermelho = (255, 10, 10)  # Definição da cor vermelha
    corFundo = (32, 33, 36)  # Definição da cor de fundo da tela
    corBorda = (42, 43, 46)  # Definição da cor da borda da tela
    corTitulo = (200, 0, 255)  # Definição da cor do título do jogo
    largura = 640  # Definição da largura da tela do jogo
    altura = 480  # Definição da altura da tela do jogo
    fps = pygame.time.Clock()  # Objeto Clock para controlar a taxa de quadros por segundo
    tela = pygame.display.set_mode((largura, altura))  # Objeto Surface que representa a janela do jogo


class Cobrinha:
    """
    Classe que representa a cobrinha do jogo Snake.

    Atributos:
    - __corCorpo: Uma tupla que define a cor do corpo da cobrinha.
    - __corCabeca: Uma tupla que define a cor da cabeça da cobrinha.
    - __corpo: Uma lista que armazena as posições do corpo da cobrinha.
    - __direcao: Uma string que representa a direção atual da cobrinha.
    - __perca: Um valor booleano que indica se a cobrinha perdeu ou não.

    Métodos:
    - setPerca(perca: bool): Define o valor de __perca.
    - getPerca(): Retorna o valor de __perca.
    - getPosCabeca(): Retorna a posição da cabeça da cobrinha.
    - setDirecao(direcao: str): Define a direção da cobrinha.
    - getDirecao(): Retorna a direção da cobrinha.
    - Move(ponto: bool): Move a cobrinha para a próxima posição de acordo com a direção atual.
    - Draw(tela): Desenha a cobrinha na tela especificada.

    """

    def __init__(self, posInicial):
        self.__corCorpo = (0, 255, 0)  # Definição da cor do corpo da cobrinha
        self.__corCabeca = (0, 230, 0)  # Definição da cor da cabeça da cobrinha
        self.__corpo = [posInicial, (posInicial[0] - 10, posInicial[1]), (posInicial[0] - 20, posInicial[1])]  # Inicialização das posições do corpo da cobrinha
        self.__direcao = None  # Direção inicial da cobrinha
        self.__perca = True  # Indicador de perda inicial como True (ainda não perdeu)

    def setPerca(self, perca: bool):
        """Define o valor de __perca."""
        self.__perca = perca

    def getPerca(self):
        """Retorna o valor de __perca."""
        return self.__perca

    def getPosCabeca(self):
        """Retorna a posição da cabeça da cobrinha."""
        return self.__corpo[0]

    def setDirecao(self, direcao: str):
        """Define a direção da cobrinha."""
        self.__direcao = direcao

    def getDirecao(self):
        """Retorna a direção da cobrinha."""
        return self.__direcao

    def Move(self, ponto: bool):
        """
        Move a cobrinha para a próxima posição de acordo com a direção atual.

        Verifica se a cobrinha atingiu alguma borda da tela ou se colidiu com seu próprio corpo.
        Se ocorrer uma dessas condições, define __perca como False (perdeu).
        Se não ocorrer nenhuma dessas condições, atualiza as posições da cobrinha.

        """
        if self.__direcao:
            x, y = self.__corpo[0]
            if self.__direcao == "cima":
                y -= 10
            elif self.__direcao == "baixo":
                y += 10
            elif self.__direcao == "esquerda":
                x -= 10
            elif self.__direcao == "direita":
                x += 10

            if x < 10 or x > 620 or y < 50 or y > 460:
                self.__perca = False

            if (x, y) in self.__corpo:
                self.__perca = False

            self.__corpo.insert(0, (x, y))

            if not ponto:
                self.__corpo.pop()

    def Draw(self, tela):
        """Desenha a cobrinha na tela especificada."""
        for pos in self.__corpo:
            if pos == self.__corpo[0]:
                pygame.draw.rect(tela, self.__corCabeca, (pos[0], pos[1], 10, 10))
            else:
                pygame.draw.rect(tela, self.__corCorpo, (pos[0], pos[1], 10, 10))


class Comida:
    """
    Classe que representa a comida do jogo Snake.

    Atributos:
    - __cor: Uma tupla que define a cor da comida.
    - __pos: Uma tupla que armazena a posição da comida.

    Métodos:
    - setPos(pos: tuple[int, int]): Define a posição da comida.
    - getPos(): Retorna a posição da comida.
    - NewPos(): Gera uma nova posição aleatória para a comida.
    - Draw(tela): Desenha a comida na tela especificada.

    """

    def __init__(self):
        self.__cor = (255, 0, 0)  # Definição da cor da comida
        self.__pos = self.NewPos()  # Geração de uma posição inicial para a comida

    def setPos(self, pos: tuple[int, int]):
        """Define a posição da comida."""
        self.__pos = pos

    def getPos(self):
        """Retorna a posição da comida."""
        return self.__pos

    def NewPos(self):
        """
        Gera uma nova posição aleatória para a comida.

        A nova posição é gerada dentro dos limites da tela, considerando o tamanho da comida.

        """
        x = random.randint(10, 620 - 10)
        y = random.randint(50, 460 - 10)
        return x // 10 * 10, y // 10 * 10

    def Draw(self, tela):
        """Desenha a comida na tela especificada."""
        pygame.draw.rect(tela, self.__cor, (self.__pos[0], self.__pos[1], 10, 10))


class ObjetoTexto:
    """
    Classe que representa um objeto de texto para exibição na tela.

    Atributos:
    - fonte: O nome do arquivo de fonte a ser utilizado.
    - tamanho: O tamanho da fonte em pixels.
    - font: O objeto de fonte do Pygame.
    - texto: O conteúdo do texto.
    - cor: A cor do texto.
    - fundo: A cor de fundo do texto (opcional).
    - largura: A largura do texto renderizado.
    - altura: A altura do texto renderizado.
    - posX: A posição X do texto na tela.
    - posY: A posição Y do texto na tela.
    - botao: O retângulo de colisão do botão (opcional).
    - render: A superfície renderizada do texto.

    Métodos:
    - Draw(): Desenha o texto na tela.
    - FormatarMeio(Y: int): Formata o texto para ficar centralizado horizontalmente com base na posição Y especificada.
    - FormatarInferorDireito(): Formata o texto para ficar alinhado no canto inferior direito da tela.
    - CriarBotao(): Cria um retângulo de colisão para o texto como um botão.
    - FormararSuperiorDireito(): Formata o texto para ficar alinhado no canto superior direito da tela.
    - FormararSuperiorEscerdo(Y: int = None): Formata o texto para ficar alinhado no canto superior esquerdo da tela.

    """

    def __init__(self, texto: str, cor: tuple[int, int, int], tamanho: int, fonte: str = None,
                 fundo: tuple[int, int, int] = None):
        self.fonte = fonte  # Nome do arquivo de fonte a ser utilizado
        self.tamanho = tamanho  # Tamanho da fonte em pixels
        self.font = pygame.font.Font(self.fonte, self.tamanho)  # Objeto de fonte do Pygame
        self.texto = texto  # Conteúdo do texto
        self.cor = cor  # Cor do texto
        self.fundo = fundo  # Cor de fundo do texto (opcional)
        self.largura, self.altura = self.font.size(self.texto)  # Largura e altura do texto renderizado
        self.posX = 1  # Posição X do texto na tela
        self.posY = 1  # Posição Y do texto na tela
        self.botao = None  # Retângulo de colisão do botão (opcional)
        if self.fundo is None:
            self.render = self.font.render(self.texto, True, self.cor)
        else:
            self.render = self.font.render(self.texto, True, self.cor, self.fundo)

    def Draw(self):
        """Desenha o texto na tela."""
        Scream.tela.blit(self.render, (self.posX, self.posY))

    def FormatarMeio(self, Y: int):
        """
        Formata o texto para ficar centralizado horizontalmente com base na posição Y especificada.

        O texto é ajustado para que seu centro esteja alinhado horizontalmente com a posição Y fornecida.

        """
        self.posX = (Scream.largura - self.largura) // 2
        self.posY = Y - (self.altura // 2)

    def FormatarInferorDireito(self):
        """Formata o texto para ficar alinhado no canto inferior direito da tela."""
        self.posX = (Scream.largura - self.largura) - 10
        self.posY = (Scream.altura - self.altura) - 10

    def CriarBotao(self):
        """Cria um retângulo de colisão para o texto como um botão."""
        self.botao = pygame.Rect(self.posX, self.posY, self.largura, self.altura)

    def FormararSuperiorDireito(self):
        """Formata o texto para ficar alinhado no canto superior direito da tela."""
        self.posX = (Scream.largura - self.largura) - 10
        self.posY = 25 - (self.altura // 2)

    def FormararSuperiorEscerdo(self, Y: int = None):
        """
        Formata o texto para ficar alinhado no canto superior esquerdo da tela.

        Se a posição Y não for fornecida, o texto será centralizado verticalmente.

        """
        self.posX = 10
        if Y is None:
            self.posY = 25 - (self.altura // 2)
        else:
            self.posY = Y - (self.altura // 2)
