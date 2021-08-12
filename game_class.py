"""Модуль, в котором инициализируется класс, контролирующий игровой процесс, а также собирающий игровую статистику."""

import random
from game_stats import GameStats
from heroes_factory import Hero
from monsters_factory import Monster, MonsterFactory, WizardFactory, GoblinFactory, SkeletonFactory, SwordsmanGoblin, ArcherSkeleton, EvilWizard
from items_factory import Item, ItemFactory, TotemFactory, AppleFactory, SpellFactory, SwordFactory, ArrowsFactory, BowFactory, Totem, Bow, Arrows, Spell, Sword
from typing import Any


class Game:
    """Класс игры."""

    def __init__(self) -> None:
        """Инициализация класса."""
        self.game_stats = GameStats(self)
        self.goblin = SwordsmanGoblin(self, self.game_stats.monster_power, self.game_stats.monster_hp)
        self.skeleton = ArcherSkeleton(self, self.game_stats.monster_power, self.game_stats.monster_hp)
        self.wizard = EvilWizard(self, self.game_stats.monster_power, self.game_stats.monster_hp)
        self.totem = Totem(self)
        self.bow = Bow(self)
        self.arrows = Arrows(self, self.game_stats.arrows_quantity, self.game_stats.arrows_power)
        self.sword = Sword(self, self.game_stats.sword_power)
        self.spell = Spell(self, self.game_stats.spell_type, self.game_stats.spell_power)
        self.hero = Hero(self)
        self.random_function = None

    def game_launch(self) -> Any:
        """Функция, реализующая запуск игры."""
        print(
            "Добро пожаловать в игру 'Герой и Чудовища 2: Волшебный тотем'!"
            "\nВам предстоит спасти королевство от нападения 10 чудовищ."
            "\nКоличество ваших жизней - 15, а сила вашей атаки - 10."
            "\nУдачи!"
        )
        self.game_stats.choose_hero()

    def object_spawner(self) -> None:
        """Генератор игровых предметов."""
        item_spawner = {
            "totem": TotemFactory,
            "apple": AppleFactory,
            "sword": SwordFactory,
            "spell": SpellFactory,
            "bow": BowFactory,
            "arrows": ArrowsFactory,
        }
        item_type_list = ["totem", "apple", "sword", "spell", "bow", "arrows"]
        spawner_type = random.choice(item_type_list)
        spawner = item_spawner[spawner_type](self)
        spawner.create_item()

    def enemy_spawner(self) -> None:
        """Генератор чудовищ."""
        monster_spawner = {
            "evil_wizard": WizardFactory,
            "skeleton_archer": SkeletonFactory,
            "swordsman_goblin": GoblinFactory,
        }
        monsters_type_list = ["evil_wizard", "skeleton_archer", "swordsman_goblin"]
        spawner_type = random.choice(monsters_type_list)
        spawner = monster_spawner[spawner_type](self)
        spawner.create_monster()

    def run_game(self) -> None:
        """Функция, реализующая игровой процесс."""
        if self.game_stats.monster_counter >= 10:
            print("Вы спасли королевство от чудовищ и победили! Поздравляем!")
            self.game_stats.reset_stats()
            exit()
        random_action_selector = [self.enemy_spawner, self.object_spawner]
        self.random_function = random.choice(random_action_selector)
        self.random_function()
