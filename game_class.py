"""
Модуль, в котором инициализируется класс игры.
Класс запускает и контролирует игровой процесс, а также собирает игровую статистику.
"""

import random
from game_stats import GameStats
from heroes_factory import Hero
from monsters_factory import Monster, MonsterFactory
from items_factory import Item, ItemFactory
from typing import Any


class Game:
    def __init__(self) -> None:
        self.game_stats = GameStats(self)
        self.item = Item(self)
        self.monster = Monster(self)
        self.hero = Hero(self)
        self.monster_factory = MonsterFactory(self)
        self.item_factory = ItemFactory(self)

    def game_launch(self) -> Any:
        """Функция, реализующая запуск игры."""
        print(
            "Добро пожаловать в игру 'Герой и Чудовища 2: Волшебный тотем'!"
            "\nВам предстоит спасти королевство от нападения 10 чудовищ."
            "\nКоличество ваших жизней - 15, а сила вашей атаки - 10."
            "\nУдачи!"
        )
        self.game_stats.choose_hero()
        self.run_game()

    def run_game(self) -> Any:
        """Функция, реализующая игровой процесс."""
        if int(self.game_stats.get_game_stats("monster_counter")) >= 10:
            print("Вы спасли королевство от чудовищ и победили! Поздравляем!")
#            self.game_stats.reset_stats()
            exit()
        else:
            spawn_monster = self.monster_factory.generate_monster
            spawn_item = self.item_factory.generate_item
            random_action_selector = [spawn_monster, spawn_item]
            random_function = random.choice(random_action_selector)
            random_function()
