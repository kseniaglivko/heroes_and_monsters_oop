"""
Фабрика по производству чудовищ.
"""

from abc import ABC, abstractmethod
from time import sleep
import random
from game_stats import get_game_stats, update_game_stats


class Monster(ABC):
    """Абстрактный класс чудовищ."""

    def __init__(self):
        super().__init__()

    @staticmethod
    def spawn():
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
    def attack(self):
        # В дальнейшем планируется выводить информацию о оставшемся здоровье у противника.
        monster_power = get_game_stats("monster", "power")
        return f"Противник атакует! Урон вашему здоровью составляет {monster_power} единиц."

    def run(self):
        print("Противник бежал!")
        sleep(1)


class EvilWizard(Monster):
    """Класс злого чародея."""

    def attack(self):
        monster_power = get_game_stats("monster", "power")
        print(f"Злой чародей атакует! Сила атаки - {monster_power}.")


class ArcherSkeleton(Monster):
    """Класс скелета-лучника."""

    def attack(self):
        monster_power = get_game_stats("monster", "power")
        return f"Скелет стреляет в вас из лука! Сила атаки - {monster_power}."


class SwordsmanGoblin(Monster):
    """Класс гоблина с мечом."""

    def attack(self):
        monster_power = get_game_stats("monster", "power")
        return f"Гоблин несется на вас с мечом! Сила атаки - {monster_power}."


class MonsterFactory(ABC):
    """Абстрактная фабрика игрового противника."""

    @abstractmethod
    def create_monster(self):
        pass


class WizardFactory(MonsterFactory):
    """Фабрика по производству злых чародеев."""

    def create_monster(self):
        power = random.randint(6, 25)
        hp = random.randint(10, 40)
        update_game_stats("monster", power, "power")
        update_game_stats("monster", "Злой колдун", "type")
        update_game_stats("monster", hp, "hp")
        return EvilWizard()


class SkeletonFactory(MonsterFactory):
    """Фабрика по производству скелетов-лучников."""

    def create_monster(self):
        power = random.randint(2, 15)
        hp = random.randint(5, 25)
        update_game_stats("monster", power, "power")
        update_game_stats("monster", "Скелет-лучник", "type")
        update_game_stats("monster", hp, "hp")
        return ArcherSkeleton()


class GoblinFactory(MonsterFactory):
    """Фабрика по производству гоблинов с мечом."""

    def create_monster(self):
        power = random.randint(4, 20)
        hp = random.randint(5, 35)
        update_game_stats("monster", power, "power")
        update_game_stats("monster", "Гоблин-мечник", "type")
        update_game_stats("monster", hp, "hp")
        return SwordsmanGoblin()
