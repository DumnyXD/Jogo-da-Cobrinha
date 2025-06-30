import pygame
from src.config.game_config import GameConfig
from src.utils.logger import Logger

logger = Logger()


class PygameRenderer:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((GameConfig.largura, GameConfig.altura))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        logger.info("PygameRenderer inicializado.")

    def render(self, game_state):
        self.screen.fill(GameConfig.corFundo)

        pygame.draw.rect(self.screen, GameConfig.corBorda, (5, 45, GameConfig.largura - 10, GameConfig.altura - 50))
        pygame.draw.rect(self.screen, GameConfig.corFundo, (10, 50, GameConfig.largura - 20, GameConfig.altura - 60))

        # Renderizar elementos do jogo (cobrinha, comida, texto)
        game_state["titulo"].Draw(self.screen)
        game_state["score"].Draw(self.screen)
        game_state["record"].Draw(self.screen)

        # Desenhar a comida
        pygame.draw.rect(self.screen, game_state["comida"].getCor(), (game_state["comida"].getPos()[0], game_state["comida"].getPos()[1], 10, 10))

        # Desenhar a cobrinha
        for pos in game_state["cobrinha"].getCorpo():
            if pos == game_state["cobrinha"].getPosCabeca():
                pygame.draw.rect(self.screen, game_state["cobrinha"].getCorCabeca(), (pos[0], pos[1], 10, 10))
            else:
                pygame.draw.rect(self.screen, game_state["cobrinha"].getCorCorpo(), (pos[0], pos[1], 10, 10))

        if game_state["pausado"]:
            game_state["texto_pausado"].Draw(self.screen)

        pygame.display.update()

    def tick(self):
        self.clock.tick(GameConfig.FPS)

    def quit(self):
        pygame.quit()
        logger.info("Pygame encerrado.")
