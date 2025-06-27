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