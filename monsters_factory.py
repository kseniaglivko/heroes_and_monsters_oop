"""
Фабрика по производству героев.
"""

from abc import ABC, abstractmethod
from time import sleep
import random
from game_stats import GameStats
from game_class import Game
from heroes_factory import Hero


class Monster(ABC):
    """Абстрактный класс чудовищ."""

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.monster_hp = hp
        self.monster_power = power
        self.game_stats = GameStats(self.game)

    @abstractmethod
    def spawn(self):
        monster_spawner = {
            "evil_wizard": WizardFactory,
            "skeleton_archer": SkeletonFactory,
            "swordsman_goblin": GoblinFactory,
        }

        monsters_type_list = ["evil_wizard", "skeleton_archer", "swordsman_goblin"]
        spawner_type = random.choice(monsters_type_list)
        spawner = monster_spawner[spawner_type]()
        monster = spawner.create_monster()
        monster.spawn()

    @abstractmethod
    def attack(self, power):
        # В дальнейшем планируется выводить информацию о оставшемся здоровье у противника.
        return f"Чудовище атаковало вас! Урон вашему здоровью составляет {power}."

    @abstractmethod
    def run(self):
        return "Чудовище убежало от вас! Отправляемся дальше."


class EvilWizard(Monster):
    """Класс злого чародея."""

    def attack(self, power):
        return f"Злой чародей атакует! Сила атаки - {power}."

    def run(self):
        return "Злой чародей убегает от вас!"


class ArcherSkeleton(Monster):
    """Класс скелета-лучника."""

    def attack(self, power):
        return f"Скелет стреляет в вас из лука! Сила атаки - {power}."

    def run(self):
        return "Скелет убегает от вас!"


class SwordsmanGoblin(Monster):
    """Класс гоблина с мечом."""

    def attack(self, power):
        return f"Гоблин несется на вас с мечом! Сила атаки - {power}."

    def run(self):
        return "Гоблин убегает от вас!"


class MonsterFactory(ABC):
    """Абстрактная фабрика игрового противника."""

    @abstractmethod
    def create_enemy(self):
        pass


class WizardFactory(MonsterFactory):
    """Фабрика по производству злых чародеев."""

    def create_monter(self):
        return EvilWizard()


class SkeletonFactory(MonsterFactory):
    """Фабрика по производству скелетов-лучников."""

    def create_monster(self):
        return ArcherSkeleton()


class GoblinFactory(MonsterFactory):
    """Фабрика по производству гоблинов с мечом."""

    def create_monster(self):
        return SwordsmanGoblin()
