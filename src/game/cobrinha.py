from src.utils.logger import Logger
from src.config.game_config import GameConfig
from src.game.move_strategy import MoveUpStrategy, MoveDownStrategy, MoveLeftStrategy, MoveRightStrategy
from src.game.position import Position

logger = Logger()


class Cobrinha:
    def __init__(self, posInicial: Position):
        self.__corCorpo = (0, 255, 0)
        self.__corCabeca = (0, 230, 0)
        self.__corpo = [posInicial, Position(posInicial.x - 10, posInicial.y), Position(posInicial.x - 20, posInicial.y)]
        self.__direcao = None
        self.__perca = True
        self.__move_strategies = {
            "cima": MoveUpStrategy(),
            "baixo": MoveDownStrategy(),
            "esquerda": MoveLeftStrategy(),
            "direita": MoveRightStrategy()
        }
        logger.info(f"Cobrinha inicializada em {posInicial}")

    def setPerca(self, perca: bool):
        self.__perca = perca

    def getPerca(self):
        return self.__perca

    def getPosCabeca(self) -> Position:
        return self.__corpo[0]

    def setDirecao(self, direcao: str):
        if self.__direcao == "cima" and direcao == "baixo":
            return
        if self.__direcao == "baixo" and direcao == "cima":
            return
        if self.__direcao == "esquerda" and direcao == "direita":
            return
        if self.__direcao == "direita" and direcao == "esquerda":
            return
        self.__direcao = direcao

    def getDirecao(self):
        return self.__direcao

    def Move(self, ponto: bool):
        if not self.__direcao:
            return

        current_pos = self.__corpo[0]
        logger.info(f"Movendo cobrinha de {current_pos} na direção {self.__direcao}")

        # Calcula a próxima posição sem criar um objeto Position ainda
        next_pos_candidate = self.__move_strategies[self.__direcao].move(current_pos)
        next_x, next_y = next_pos_candidate.x, next_pos_candidate.y

        if self._check_collision(next_x, next_y):
            self.__perca = False
            logger.warning(f"Cobrinha colidiu em ({next_x},{next_y}). Game Over!")
            return

        # Somente cria o objeto Position se a posição for válida
        new_pos = Position(next_x, next_y)
        self.__corpo.insert(0, new_pos)

        if not ponto:
            self.__corpo.pop()
        logger.info(f"Cobrinha movida para {new_pos}. Ponto: {ponto}")

    def _check_collision(self, x: int, y: int) -> bool:
        # Colisão com as bordas
        if not (10 <= x <= GameConfig.largura - 20 and 50 <= y <= GameConfig.altura - 20):
            return True
        
        # Colisão com o próprio corpo
        # Converte a tupla (x,y) para um objeto Position para comparação
        test_pos = Position(x, y)
        if test_pos in self.__corpo[1:]:
            return True
        return False

    def getCorpo(self):
        return self.__corpo

    def getCorCabeca(self):
        return self.__corCabeca

    def getCorCorpo(self):
        return self.__corCorpo