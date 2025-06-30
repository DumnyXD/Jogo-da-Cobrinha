from src.utils.logger import Logger

logger = Logger()

class ScoreManager:
    def __init__(self, initial_high_score: int):
        self._current_score = 0
        self._high_score = initial_high_score
        logger.info(f"ScoreManager inicializado com high_score: {initial_high_score}")

    def add_score(self, points: int):
        self._current_score += points
        logger.info(f"Pontuação atualizada: {self._current_score}")
        if self._current_score > self._high_score:
            self._high_score = self._current_score
            logger.info(f"Nova maior pontuação: {self._high_score}")

    def get_current_score(self) -> int:
        return self._current_score

    def get_high_score(self) -> int:
        return self._high_score

    def reset_score(self):
        self._current_score = 0
        logger.info("Pontuação resetada.")
