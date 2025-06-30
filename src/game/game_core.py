
import random
from src.game.cobrinha import Cobrinha
from src.game.comida import Comida
from src.graphics.objeto_texto import ObjetoTexto
from src.config.game_config import GameConfig
from src.utils.logger import Logger

logger = Logger()


class GameCore:
    def __init__(self, maiorPontuacao):
        self.maiorPontuacao = maiorPontuacao
        self.pontuacao = 0
        self.comida = Comida()
        self.cobrinha = Cobrinha((100, 100))
        self.pausado = False

        self.titulo = ObjetoTexto("Snake", GameConfig.corTitulo, 25, "Daydream.ttf")
        self.titulo.FormatarMeio(25)

        self.texto_pausado = ObjetoTexto("PAUSADO", GameConfig.branco, 40, "Daydream.ttf")
        self.texto_pausado.FormatarMeio(GameConfig.altura // 2)

        logger.info("GameCore inicializado.")

    def update(self, actions):
        for action in actions:
            logger.info(f"Ação recebida: {action}")
            if action == "toggle_pause":
                self.pausado = not self.pausado
                logger.info(f"Jogo {'PAUSADO' if self.pausado else 'RESUMIDO'}.")

            if not self.pausado:
                if action == "move_up" and self.cobrinha.getDirecao() != "baixo":
                    self.cobrinha.setDirecao("cima")
                    logger.info("Direção da cobrinha alterada para CIMA.")
                elif action == "move_down" and self.cobrinha.getDirecao() != "cima":
                    self.cobrinha.setDirecao("baixo")
                    logger.info("Direção da cobrinha alterada para BAIXO.")
                elif action == "move_left" and self.cobrinha.getDirecao() != "direita" and self.cobrinha.getDirecao() is not None:
                    self.cobrinha.setDirecao("esquerda")
                    logger.info("Direção da cobrinha alterada para ESQUERDA.")
                elif action == "move_right" and self.cobrinha.getDirecao() != "esquerda":
                    self.cobrinha.setDirecao("direita")
                    logger.info("Direção da cobrinha alterada para DIREITA.")

        if not self.pausado:
            if self.comida.getPos() == self.cobrinha.getPosCabeca():
                logger.info("Comida consumida!")
                ponto = True
                self.pontuacao += 10
                self.comida.setPos(self.comida.NewPos())
                logger.info(f"Nova pontuação: {self.pontuacao}. Nova posição da comida: {self.comida.getPos()}")
                if self.maiorPontuacao < self.pontuacao:
                    self.maiorPontuacao = self.pontuacao
                    logger.info(f"Nova maior pontuação: {self.maiorPontuacao}")
            else:
                ponto = False

            self.cobrinha.Move(ponto)

            if not self.cobrinha.getPerca():
                logger.info(f"Game Over! Pontuação final: {self.pontuacao}. Maior pontuação: {self.maiorPontuacao}")
                return "game_over"
        return "running"

    def get_game_state(self):
        score_text = ObjetoTexto(f"score: {self.pontuacao}", GameConfig.branco, 17, "Daydream.ttf")
        score_text.FormararSuperiorDireito()

        record_text = ObjetoTexto(f"record: {self.maiorPontuacao}", GameConfig.branco, 17, "Daydream.ttf")
        record_text.FormararSuperiorEscerdo()

        return {
            "titulo": self.titulo,
            "score": score_text,
            "record": record_text,
            "comida": self.comida,
            "cobrinha": self.cobrinha,
            "pausado": self.pausado,
            "texto_pausado": self.texto_pausado
        }
