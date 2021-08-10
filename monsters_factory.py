"""
Фабрика по производству чудовищ.
"""

from abc import ABC, abstractmethod
from time import sleep
import random


class Monster(ABC):
    """Абстрактный класс чудовищ."""

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.game_stats = self.game.game_stats

    @abstractmethod
    def spawn(self):
        monster_spawner = {
            "evil_wizard": WizardFactory,
            "skeleton_archer": SkeletonFactory,
            "swordsman_goblin": GoblinFactory,
        }
        monsters_type_list = ["evil_wizard", "skeleton_archer", "swordsman_goblin"]
        spawner_type = random.choice(monsters_type_list)
        spawner = monster_spawner[spawner_type](self.game)
        monster = spawner.create_monster()
        monster.spawn()

    @abstractmethod
    def attack(self):
        monster_power = self.game_stats.get_game_stats("monster", "power")
        print(
            f"Противник атакует! Урон вашему здоровью составляет {monster_power} единиц."
        )

    @abstractmethod
    def be_attacked(self):
        pass

    @staticmethod
    def run():
        print("Противник бежал!")
        sleep(1)


class EvilWizard(Monster):
    """Класс злого чародея."""

    def __init__(self, game, power, hp):
        self.game = game
        super().__init__(self.game)
        self.game_stats = self.game.game_stats
        self.power = power
        self.hp = hp

    def spawn(self):
        print(
            f"Перед вами возник злой чародей! Его мощь - {self.power}, а запас здоровья - {self.hp}."
        )

    def attack(self):
        print(
            f"Злой чародей атакует! Урон вашему здоровью составляет {self.power} единиц."
        )

    def be_attacked(self):
        hero_attack = self.game_stats.get_game_stats("hero", "power")
        updated_hp = self.hp - hero_attack
        self.game_stats.update_game_stats("monster", updated_hp, "hp")
        self.hp = updated_hp
        print(
            f"Злой колдун морщится от боли! Он потерял {hero_attack} здоровья."
            f"Здоровья осталось {updated_hp} "
        )


class ArcherSkeleton(Monster):
    """Класс скелета-лучника."""

    def __init__(self, game, power, hp):
        self.game = game
        super().__init__(self.game)
        self.game_stats = self.game.game_stats
        self.power = power
        self.hp = hp

    def spawn(self):
        print(
            f"Вам на пути попался скелет-лучник! Его мощь - {self.power}, а запас здоровья - {self.hp}."
        )

    def attack(self):
        print(
            f"Скелет стреляет в вас из лука! Урон вашему здоровью составляет {self.power} единиц."
        )

    def be_attacked(self):
        hero_attack = self.game_stats.get_game_stats("hero", "power")
        updated_hp = self.hp - hero_attack
        self.game_stats.update_game_stats("monster", updated_hp, "hp")
        self.hp = updated_hp
        print(
            f"Из скелета вылетают кости! Он потерял {hero_attack} здоровья."
            f"Здоровья осталось {updated_hp} "
        )


class SwordsmanGoblin(Monster):
    """Класс гоблина с мечом."""

    def __init__(self, game, power, hp):
        self.game = game
        super().__init__(self.game)
        self.game_stats = self.game.game_stats
        self.power = power
        self.hp = hp

    def spawn(self):
        print(
            f"Внезапно на вас выбегает гоблин с мечом! Его мощь - {self.power}, а запас здоровья - {self.hp}."
        )

    def attack(self):
        print(
            f"Гоблин несется на вас с мечом! Урон вашему здоровью составляет {self.power} единиц."
        )

    def be_attacked(self):
        hero_attack = self.game_stats.get_game_stats("hero", "power")
        updated_hp = self.hp - hero_attack
        self.game_stats.update_game_stats("monster", updated_hp, "hp")
        self.hp = updated_hp
        print(
            f"Злой колдун морщится от боли! Он потерял {hero_attack} здоровья."
            f"Здоровья осталось {updated_hp} "
        )


class MonsterFactory(ABC):
    """Абстрактная фабрика игрового противника."""

    def __init__(self, game):
        self.game = game
        super().__init__(self.game)

    @abstractmethod
    def create_monster(self):
        pass


class WizardFactory(MonsterFactory):
    """Фабрика по производству злых чародеев."""

    def __init__(self, game):
        self.game = game
        super().__init__(self.game)
        self.game_stats = self.game.game_stats

    def create_monster(self):
        power = random.randint(6, 25)
        hp = random.randint(10, 40)
        self.game_stats.update_game_stats("monster", power, "power")
        self.game_stats.update_game_stats("monster", hp, "hp")
        return EvilWizard(self.game, power, hp)


class SkeletonFactory(MonsterFactory):
    """Фабрика по производству скелетов-лучников."""

    def __init__(self, game):
        self.game = game
        super().__init__(self.game)
        self.game_stats = self.game.game_stats

    def create_monster(self):
        power = random.randint(2, 15)
        hp = random.randint(5, 25)
        self.game_stats.update_game_stats("monster", power, "power")
        self.game_stats.update_game_stats("monster", hp, "hp")
        return ArcherSkeleton(self.game, power, hp)


class GoblinFactory(MonsterFactory):
    """Фабрика по производству гоблинов с мечом."""

    def __init__(self, game):
        self.game = game
        super().__init__(self.game)
        self.game_stats = self.game.game_stats

    def create_monster(self):
        power = random.randint(4, 20)
        hp = random.randint(5, 35)
        self.game_stats.update_game_stats("monster", power, "power")
        self.game_stats.update_game_stats("monster", hp, "hp")
        return SwordsmanGoblin(self.game, power, hp)
