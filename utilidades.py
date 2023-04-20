import pygame
from tela import tela


def CriarTexto(texto: str, cor: tuple[int, int, int], tamanho: int, fundo=None, ):
    font = pygame.font.Font("Daydream.ttf", tamanho)
    if fundo is not None:
        palavra = font.render(texto, True, cor, fundo)
    else:
        palavra = font.render(texto, True, cor)

    largura, altura = font.size(texto)
    return palavra, largura, altura


def PosTextoMeio(sizeTexto: tuple[int, int], posY: int):
    textoX = (tela.largura - sizeTexto[0]) //2
    textoY = posY - (sizeTexto[1] // 2)
    return textoX, textoY
