import random
import pygame
#Fernanda

class Scream:
    """Aqui está todas as definições que envolve a tela, incluindo as cores que vão ser usadas"""
    # cores
    verde = (10, 255, 10)
    branco = (255, 255, 255)
    vermelho = (255, 10, 10)
    corFundo = (32, 33, 36)
    corBorda = (42, 43, 46)
    corTitulo = (200, 0, 255)

    largura = 640
    altura = 480
    fps = pygame.time.Clock()
    tela = pygame.display.set_mode((largura, altura))


class Cobrinha:
    def __init__(self, posInicial):
        self.__corCorpo = (0, 255, 0)
        self.__corCabeca = (0, 230, 0)
        self.__tamanho = 10
        self.__corpo = [posInicial, (posInicial[0] - 10, posInicial[1]), (posInicial[0] - 20, posInicial[1])]
        self.__direcao = None
        self.__perca = True

    def setPerca(self, perca: bool):
        self.__perca = perca

    def getPerca(self):
        return self.__perca

    def getPosCabeca(self):
        return self.__corpo[0]

    def setDirecao(self, direcao: str):
        self.__direcao = direcao

    def getDirecao(self):
        return self.__direcao

    def Move(self, ponto: bool):
        if self.__direcao:
            x, y = self.__corpo[0]
            if self.__direcao == "cima":
                y -= self.__tamanho
            elif self.__direcao == "baixo":
                y += self.__tamanho
            elif self.__direcao == "esquerda":
                x -= self.__tamanho
            elif self.__direcao == "direita":
                x += self.__tamanho

            if x < 10:
                self.__perca = False
            elif x > 620:
                self.__perca = False
            elif y < 50:
                self.__perca = False
            elif y > 460:
                self.__perca = False

            if (x, y) in self.__corpo:
                self.__perca = False

            self.__corpo.insert(0, (x, y))

            if not ponto:
                self.__corpo.pop()

    def Draw(self, tela):
        for pos in self.__corpo:
            if pos == self.__corpo[0]:
                pygame.draw.rect(tela, self.__corCabeca, (pos[0], pos[1], self.__tamanho, self.__tamanho))

            else:
                pygame.draw.rect(tela, self.__corCorpo, (pos[0], pos[1], self.__tamanho, self.__tamanho))


class Comida:

    def __init__(self):
        self.__cor = (255, 0, 0)
        self.__pos = self.NewPos()

    def setPos(self, pos: tuple[int, int]):
        self.__pos = pos

    def getPos(self):
        return self.__pos

    def NewPos(self):
        x = random.randint(10, 620 - 10)
        y = random.randint(50, 460 - 10)
        return x // 10 * 10, y // 10 * 10

    def Draw(self, tela):
        pygame.draw.rect(tela, self.__cor, (self.__pos[0], self.__pos[1], 10, 10))


class ObjetoTexto:
    def __init__(self, texto: str, cor: tuple[int, int, int], tamanho: int, fonte: str = None,
                 fundo: tuple[int, int, int] = None):
        self.fonte = fonte
        self.tamanho = tamanho
        self.font = pygame.font.Font(self.fonte, self.tamanho)
        self.texto = texto
        self.cor = cor
        self.fundo = fundo
        self.largura, self.altura = self.font.size(self.texto)
        self.posX = 1
        self.posY = 1
        self.botao = None
        if self.fundo is None:
            self.render = self.font.render(self.texto, True, self.cor)
        else:
            self.render = self.font.render(self.texto, True, self.cor, self.fundo)

    def Draw(self):
        Scream.tela.blit(self.render, (self.posX, self.posY))

    def FormatarMeio(self, Y: int):
        self.posX = (Scream.largura - self.largura) // 2
        self.posY = Y - (self.altura // 2)

    def FormatarInferorDireito(self):
        self.posX = (Scream.largura - self.largura) - 20
        self.posY = (Scream.altura - self.altura) - 20

    def CriarBotao(self):
        self.botao = pygame.Rect(self.posX, self.posY, self.largura, self.altura)

