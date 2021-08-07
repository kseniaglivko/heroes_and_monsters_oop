"""
Модуль, в котором инициализируется класс игры.
Класс запускает и контролирует игровой процесс, а также собирает игровую статистику.
"""

from game_stats import GameStats
from heroes_factory import Hero
from monsters_factory import Monster, WizardFactory, SkeletonFactory, GoblinFactory
from items_factory import Totem, Apple, Sword, Spell, Bow, Arrows, TotemFactory, AppleFactory, SwordFactory, SpellFactory, BowFactory, ArrowsFactory
import random


class Game:
    def __init__(self):

        self.game_stats = GameStats(self)
        self.hero = Hero(self)
        self.monster = Monster(self)
        self.Item = Item(self)

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

    def _spawn_items(self):
        item = Item()
# item_spawning = {
#    "totem": TotemFactory,
#    "apple": AppleFactory,
#    "sword": SwordFactory,
#    "spell": SpellFactory,
#    "bow": BowFactory,
#    "arrows": ArrowsFactory,
# }


# item_type_list = ["totem", "apple", "sword, "spell", "bow", "arrows"]

# for i in range(10):
#    spawner_type = random.choice(item_type_list)

#    spawner = item_spawner[spawner_type]()


#    item = spawner.create_item()
