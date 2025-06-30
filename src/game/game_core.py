import random
from src.game.cobrinha import Cobrinha
from src.game.comida import Comida
from src.config.game_config import GameConfig
from src.utils.logger import Logger
from src.game.score_manager import ScoreManager
from src.game.game_observer import GameObserver
from src.game.position import Position

logger = Logger()


class GameCore:
    def __init__(self, maiorPontuacao):
        self.score_manager = ScoreManager(maiorPontuacao)
        self.comida = Comida()
        self.cobrinha = Cobrinha(Position(100, 100))
        self.pausado = False
        self._observers = []

        logger.info("GameCore inicializado.")

    def add_observer(self, observer: GameObserver):
        self._observers.append(observer)

    def remove_observer(self, observer: GameObserver):
        self._observers.remove(observer)

    def _notify_observers(self):
        game_state = self.get_game_state()
        for observer in self._observers:
            observer.update(game_state)

    def update(self, actions):
        direction_changed_this_frame = False
        for action in actions:
            logger.info(f"Ação recebida: {action}")
            if action == "toggle_pause":
                self.pausado = not self.pausado
                logger.info(f"Jogo {'PAUSADO' if self.pausado else 'RESUMIDO'}.")

            if not self.pausado:
                if not direction_changed_this_frame:
                    if action == "move_up" and self.cobrinha.getDirecao() != "baixo":
                        self.cobrinha.setDirecao("cima")
                        direction_changed_this_frame = True
                        logger.info("Direção da cobrinha alterada para CIMA.")
                    elif action == "move_down" and self.cobrinha.getDirecao() != "cima":
                        self.cobrinha.setDirecao("baixo")
                        direction_changed_this_frame = True
                        logger.info("Direção da cobrinha alterada para BAIXO.")
                    elif action == "move_left" and self.cobrinha.getDirecao() != "direita" and self.cobrinha.getDirecao() is not None:
                        self.cobrinha.setDirecao("esquerda")
                        direction_changed_this_frame = True
                        logger.info("Direção da cobrinha alterada para ESQUERDA.")
                    elif action == "move_right" and self.cobrinha.getDirecao() != "esquerda":
                        self.cobrinha.setDirecao("direita")
                        direction_changed_this_frame = True
                        logger.info("Direção da cobrinha alterada para DIREITA.")

        if not self.pausado:
            ponto = False
            if self.comida.getPos() == self.cobrinha.getPosCabeca():
                logger.info("Comida consumida!")
                ponto = True
                self.score_manager.add_score(10)
                self.comida.setPos(self.comida.NewPos())
                logger.info(f"Nova pontuação: {self.score_manager.get_current_score()}. Nova posição da comida: {self.comida.getPos()}")

            self.cobrinha.Move(ponto)

            if not self.cobrinha.getPerca():
                logger.info(f"Game Over! Pontuação final: {self.score_manager.get_current_score()}. Maior pontuação: {self.score_manager.get_high_score()}")
                return "game_over"
        
        self._notify_observers()
        return "running"

    def get_game_state(self):
        return {
            "current_score": self.score_manager.get_current_score(),
            "high_score": self.score_manager.get_high_score(),
            "comida": self.comida,
            "cobrinha": self.cobrinha,
            "pausado": self.pausado,
        }

    def get_high_score(self):
        return self.score_manager.get_high_score()