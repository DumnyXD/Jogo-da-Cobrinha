import pygame


class Cobrinha:
    def __init__(self, corCabeca, corCorpo, posInicial):
        self.__corCorpo = corCorpo
        self.__corCabeca = corCabeca
        self.__tamanho = 10
        self.__corpo = [posInicial, (posInicial[0] - 10, posInicial[1]), (posInicial[0] - 20, posInicial[1])]
        self.__direcao = None
        self.__perca = True

    def setPerca(self, perca:bool):
        self.__perca = perca
    def getPerca(self):
        return self.__perca

    def getPosCabeca(self):
        return self.__corpo[0]

    def setDirecao(self,direcao:str):
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

            if (x, y) in self.__corpo:
                self.__perca = False

            self.__corpo.insert(0, (x, y))
            if not ponto:
                self.__corpo.pop()

    def ChecarPerca(self):
        x, y = self.__corpo[0]
        if x < 10:
            self.__perca = False
        elif x > 620:
            self.__perca = False
        elif y < 50:
            self.__perca = False
        elif y > 460:
            self.__perca = False

    def Draw(self, tela):
        for pos in self.__corpo:
            if pos == self.__corpo[0]:
                pygame.draw.rect(tela, self.__corCabeca, (pos[0], pos[1], self.__tamanho, self.__tamanho))

            else:
                pygame.draw.rect(tela, self.__corCorpo, (pos[0], pos[1], self.__tamanho, self.__tamanho))
