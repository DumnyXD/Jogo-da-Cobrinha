import pygame
from telas import jogo
from pygame.locals import *
import sys

pygame.init()

larguraTela = 640
alturaTela = 480
tela = pygame.display.set_mode((larguraTela, alturaTela))

fonteMenu = pygame.font.Font("Daydream.ttf", 36)

textoIniciar = fonteMenu.render("Iniciar", True, (0, 200, 0))
textoCreditos = fonteMenu.render("Créditos", True, (0, 100, 0))
textoSair = fonteMenu.render("Sair", True, (255, 10, 10))

# posIni
