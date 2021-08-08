"""
Модуль, в котором инициализируется класс игры.
Класс запускает и контролирует игровой процесс, а также собирает игровую статистику.
"""

import random
from game_stats import GameStats, get_game_stats, reset_stats
from heroes_factory import Hero
from monsters_factory import Monster, WizardFactory, SkeletonFactory, GoblinFactory
from items_factory import (
    Item,
    TotemFactory,
    AppleFactory,
    SwordFactory,
    SpellFactory,
    BowFactory,
    ArrowsFactory,
)


class Game:
    def __init__(self):

        self.game_stats = GameStats(self)
        self.hero = Hero(self)
        self.monster = Monster(self)
        self.Item = Item(self)

    def game_launch(self):
        reset_stats()
        print(
            "Добро пожаловать в игру 'Герой и Чудовища 2: Волшебный тотем'!"
            "\nВам предстоит спасти королевство от нападения 10 чудовищ."
            "\nКоличество ваших жизней - 15, а сила вашей атаки - 10."
            "\nУдачи!"
        )
        self.game_stats.choose_hero()
        self.run_game()

    def run_game(self):
        if get_game_stats("monster_counter") >= 10:
            print("Вы спасли королевство от чудовищ и победили! Поздравляем!")
            exit()
        else:
            random_action_selector = [self.spawn_monsters, self.spawn_items]
            random_function = random.choice(random_action_selector)
            random_function()

    def spawn_monsters(self):
        monster = Monster()
        monster_spawner = {
            "evil_wizard": WizardFactory,
            "skeleton_archer": SkeletonFactory,
            "swordsman_goblin": GoblinFactory,
        }

        monsters_type_list = ["evil_wizard", "skeleton_archer", "swordsman_goblin"]

        for i in range(10):
            spawner_type = random.choice(monsters_type_list)
            spawner = monster_spawner[spawner_type]()
            monster = spawner.create_monster()
            monster.spawn()

    def spawn_items(self):
        item = Item()
        item_spawner = {
            "totem": TotemFactory,
            "apple": AppleFactory,
            "sword": SwordFactory,
            "spell": SpellFactory,
            "bow": BowFactory,
            "arrows": ArrowsFactory,
        }
        item_type_list = ["totem", "apple", "sword", "spell", "bow", "arrows"]
        for i in range(10):
            spawner_type = random.choice(item_type_list)
            spawner = item_spawner[spawner_type]()
            item = spawner.create_item()
            item.spawn()
