import pygame
from src.config.game_config import GameConfig
from src.utils.logger import Logger
from src.graphics.objeto_texto import ObjetoTexto
from src.game.game_observer import GameObserver

logger = Logger()


class PygameRenderer(GameObserver):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((GameConfig.largura, GameConfig.altura))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        logger.info("PygameRenderer inicializado.")

    def update(self, game_state):
        self.render(game_state)

    def render(self, game_state):
        self.screen.fill(GameConfig.corFundo)

        pygame.draw.rect(self.screen, GameConfig.corBorda, (5, 45, GameConfig.largura - 10, GameConfig.altura - 50))
        pygame.draw.rect(self.screen, GameConfig.corFundo, (10, 50, GameConfig.largura - 20, GameConfig.altura - 60))

        # Renderizar elementos do jogo (cobrinha, comida, texto)
        titulo = ObjetoTexto("Snake", GameConfig.corTitulo, 25, "Daydream.ttf")
        titulo.FormatarMeio(25)
        titulo.Draw(self.screen)

        score_text = ObjetoTexto(f"score: {game_state['current_score']}", GameConfig.branco, 17, "Daydream.ttf")
        score_text.FormararSuperiorDireito()
        score_text.Draw(self.screen)

        record_text = ObjetoTexto(f"record: {game_state['high_score']}", GameConfig.branco, 17, "Daydream.ttf")
        record_text.FormararSuperiorEscerdo()
        record_text.Draw(self.screen)

        # Desenhar a comida
        pygame.draw.rect(self.screen, game_state["comida"].getCor(), (game_state["comida"].getPos().x, game_state["comida"].getPos().y, 10, 10))

        # Desenhar a cobrinha
        for pos in game_state["cobrinha"].getCorpo():
            if pos == game_state["cobrinha"].getPosCabeca():
                pygame.draw.rect(self.screen, game_state["cobrinha"].getCorCabeca(), (pos.x, pos.y, 10, 10))
            else:
                pygame.draw.rect(self.screen, game_state["cobrinha"].getCorCorpo(), (pos.x, pos.y, 10, 10))

        if game_state["pausado"]:
            texto_pausado = ObjetoTexto("PAUSADO", GameConfig.branco, 40, "Daydream.ttf")
            texto_pausado.FormatarMeio(GameConfig.altura // 2)
            texto_pausado.Draw(self.screen)

        pygame.display.update()

    def tick(self):
        self.clock.tick(GameConfig.FPS)

    def quit(self):
        pygame.quit()
        logger.info("Pygame encerrado.")
