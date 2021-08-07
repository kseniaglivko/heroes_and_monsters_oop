"""
Модуль, в котором инициализируется класс игры.
Класс запускает и контролирует игровой процесс, а также собирает игровую статистику.
"""

from game_stats import GameStats
from heroes_factory import Hero
from monsters_factory import Monster, WizardFactory, SkeletonFactory, GoblinFactory
import random


class Game:
    def __init__(self):

        self.game_stats = GameStats(self)
        self.hero = Hero()
        # monsters, weapons, etc.

    def run_game(self):
        while True:
            if self.game_stats.game_active:
                pass

    def _game_lunch(self):
        self.game_stats.reset_stats()
        self._spawn_monsters()

    def _spawn_monsters(self):
        monster = Monster()
# monster_spawning = {
#    "evil_wizard" : WizardFactory,
#    "skeleton_archer" : SkeletonFactory,
#    "swordsman_goblin" : GoblinFactory
# }


# monsters_type_list = ["evil_wizard", "skeleton_archer", "swordsman_goblin"]

# for i in range(10):
#    spawner_type = random.choice(monsters_type_list)

#    spawner = monster_spawner[spawner_type]()


#    enemy = spawner.create_monster()
#    action = monster.attack()
#    print(action)
