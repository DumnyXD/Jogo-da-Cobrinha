import pygame
from src.utils.logger import Logger

logger = Logger()


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
        logger.info(f"Cobrinha inicializada em {posInicial}")

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
            logger.info(f"Movendo cobrinha de ({x},{y}) na direção {self.__direcao}")
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
                logger.warning(f"Cobrinha colidiu com a borda em ({x},{y}). Game Over!")

            if (x, y) in self.__corpo:
                self.__perca = False
                logger.warning(f"Cobrinha colidiu com o próprio corpo em ({x},{y}). Game Over!")

            self.__corpo.insert(0, (x, y))

            if not ponto:
                self.__corpo.pop()
            logger.info(f"Cobrinha movida para ({x},{y}). Ponto: {ponto}")

    def Draw(self, tela):
        """Desenha a cobrinha na tela especificada."""
        for pos in self.__corpo:
            if pos == self.__corpo[0]:
                pygame.draw.rect(tela, self.__corCabeca, (pos[0], pos[1], 10, 10))
            else:
                pygame.draw.rect(tela, self.__corCorpo, (pos[0], pos[1], 10, 10))