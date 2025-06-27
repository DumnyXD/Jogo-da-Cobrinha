import pygame
import os
from src.config.game_config import Scream
from src.utils.logger import Logger

logger = Logger()


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
        font_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'assets', self.fonte)
        self.font = pygame.font.Font(font_path, self.tamanho)  # Objeto de fonte do Pygame
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
        logger.info(f"ObjetoTexto criado: \"{self.texto}\" (Tamanho: {self.tamanho}, Cor: {self.cor})")

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