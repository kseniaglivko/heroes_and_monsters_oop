"""
Фабрика по производству чудовищ.
"""

from abc import ABC, abstractmethod
from time import sleep
import random
from typing import Any


class Monster(ABC):
    """Абстрактный класс чудовищ."""

    def __init__(self, game: Any) -> None:
        super().__init__()
        self.game = game
        self.game_stats = self.game.game_stats
#        self.hero = self.game.hero

    def spawn(self) -> None:
        """Появление чудовища."""
        print("Перед вами появилось чудовище!")

    def attack(self) -> None:
        """Функция атаки чудовища."""
        monster_power = self.game_stats.get_game_stats("monster", "power")
        print(
            f"Противник атакует! Урон вашему здоровью составляет {monster_power} единиц."
        )

    def be_attacked(self) -> None:
        """Функция реакции чудовища на атаку героя."""
        pass

    @staticmethod
    def run() -> None:
        """Функция реализации побега чудовища."""
        print("Противник бежал!")
        sleep(1)


class EvilWizard(Monster):
    """Класс злого чародея."""

    def __init__(self, game: Any, power: int, hp: int) -> None:
        self.game = game
        super().__init__(self.game)
        self.game_stats = self.game.game_stats
        self.power = power
        self.hp = hp

    def spawn(self) -> None:
        """Появление злого чародея."""
        print(
            f"Перед вами возник злой чародей! Его мощь - {self.power}, а запас здоровья - {self.hp}."
        )

    def attack(self) -> None:
        """Функция атаки чародея."""
        print(
            f"Злой чародей атакует! Урон вашему здоровью составляет {self.power} единиц."
        )
        self.game.hero.be_attacked()

    def be_attacked(self) -> None:
        """Функция реакции чародея на атаку героя."""
        hero_attack = int(self.game_stats.get_game_stats("hero", "power"))
        updated_hp = int(self.hp) - hero_attack
        self.game_stats.update_game_stats("monster", updated_hp, "hp")
        self.hp = updated_hp
        if updated_hp <= 0:
            print("Победа! Чародей пал! Движемся дальше...")
            sleep(1)
            self.game.run_game()
        print(
            f"Злой колдун морщится от боли! Он потерял {hero_attack} здоровья."
            f"Здоровья осталось {updated_hp} ."
        )
        self.attack()


class ArcherSkeleton(Monster):
    """Класс скелета-лучника."""

    def __init__(self, game: Any, power: int, hp: int) -> None:
        self.game = game
        super().__init__(self.game)
        self.game_stats = self.game.game_stats
        self.power = power
        self.hp = hp

    def spawn(self) -> None:
        """Появление скелета-лучника."""
        print(
            f"Вам на пути попался скелет-лучник! Его мощь - {self.power}, а запас здоровья - {self.hp}."
        )

    def attack(self) -> None:
        """Функция атаки скелета-лучника."""
        print(
            f"Скелет стреляет в вас из лука! Урон вашему здоровью составляет {self.power} единиц."
        )
        self.game.hero.be_attacked()

    def be_attacked(self) -> None:
        """Функция реакции скелета-лучника на атаку героя."""
        hero_attack = int(self.game_stats.get_game_stats("hero", "power"))
        updated_hp = int(self.hp) - hero_attack
        self.game_stats.update_game_stats("monster", updated_hp, "hp")
        self.hp = updated_hp
        if updated_hp <= 0:
            print("Победа! Скелет развалился на части! Движемся дальше...")
            sleep(1)
            self.game.run_game()
        print(
            f"Из скелета вылетают кости! Он потерял {hero_attack} здоровья."
            f"Здоровья осталось {updated_hp} ."
        )
        self.attack()


class SwordsmanGoblin(Monster):
    """Класс гоблина с мечом."""

    def __init__(self, game: Any, power: int, hp: int) -> None:
        self.game = game
        super().__init__(self.game)
        self.game_stats = self.game.game_stats
        self.power = power
        self.hp = hp

    def spawn(self) -> None:
        """Появление гоблина."""
        print(
            f"Внезапно на вас выбегает гоблин с мечом! Его мощь - {self.power}, а запас здоровья - {self.hp}."
        )

    def attack(self) -> None:
        """Функция атаки гоблина."""
        print(
            f"Гоблин несется на вас с мечом! Урон вашему здоровью составляет {self.power} единиц."
        )
        self.game.hero.be_attacked()

    def be_attacked(self) -> None:
        """Функция реакции гоблина на атаку героя."""
        hero_attack = int(self.game_stats.get_game_stats("hero", "power"))
        updated_hp = int(self.hp) - hero_attack
        self.game_stats.update_game_stats("monster", updated_hp, "hp")
        self.hp = updated_hp
        if self.hp <= 0:
            print("Победа! Гоблин повержен! Движемся дальше...")
            sleep(1)
            self.game.run_game()
        print(
            f"Гоблин ранен! Он потерял {hero_attack} здоровья."
            f"Здоровья осталось {updated_hp}. "
        )
        self.attack()


class MonsterFactory(ABC):
    """Абстрактная фабрика игрового противника."""

    def __init__(self, game: Any) -> None:
        self.game = game
        super().__init__()

    def generate_monster(self) -> None:
        """Генератор чудовищ."""
        monster_spawner = {
            "evil_wizard": WizardFactory,
            "skeleton_archer": SkeletonFactory,
            "swordsman_goblin": GoblinFactory,
        }
        monsters_type_list = ["evil_wizard", "skeleton_archer", "swordsman_goblin"]
        spawner_type = random.choice(monsters_type_list)
        spawner = monster_spawner[spawner_type](self.game)
        spawner.create_monster()

    def create_monster(self) -> object:
        """Создание чудовища."""
        pass


class WizardFactory(MonsterFactory):
    """Фабрика по производству злых чародеев."""

    def __init__(self, game: Any) -> None:
        self.game = game
        super().__init__(self.game)
        self.game_stats = self.game.game_stats

    def create_monster(self) -> object:
        power = random.randint(6, 25)
        hp = random.randint(10, 40)
        self.game_stats.update_game_stats("monster", power, "power")
        self.game_stats.update_game_stats("monster", hp, "hp")
        return EvilWizard(self.game, power, hp)


class SkeletonFactory(MonsterFactory):
    """Фабрика по производству скелетов-лучников."""

    def __init__(self, game: Any) -> None:
        self.game = game
        super().__init__(self.game)
        self.game_stats = self.game.game_stats

    def create_monster(self) -> object:
        power = random.randint(2, 15)
        hp = random.randint(5, 25)
        self.game_stats.update_game_stats("monster", power, "power")
        self.game_stats.update_game_stats("monster", hp, "hp")
        return ArcherSkeleton(self.game, power, hp)


class GoblinFactory(MonsterFactory):
    """Фабрика по производству гоблинов с мечом."""

    def __init__(self, game: Any) -> None:
        self.game = game
        super().__init__(self.game)
        self.game_stats = self.game.game_stats

    def create_monster(self) -> object:
        power = random.randint(4, 20)
        hp = random.randint(5, 35)
        self.game_stats.update_game_stats("monster", power, "power")
        self.game_stats.update_game_stats("monster", hp, "hp")
        return SwordsmanGoblin(self.game, power, hp)
