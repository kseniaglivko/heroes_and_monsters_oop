"""
Модуль, в котором инициализируется класс игры.
Класс запускает и контролирует игровой процесс, а также собирает игровую статистику.
"""

from game_stats import GameStats
from heroes_factory import Hero


class Game:
    def __init__(self):

        self.game_stats = GameStats()
        self.hero = Hero()
        # monsters, weapons, etc.

    def run_game(self):

        while True:
            if self.game_stats.game_active:
                pass
