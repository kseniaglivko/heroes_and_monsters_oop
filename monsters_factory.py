"""Фабрика по производству чудовищ."""

from time import sleep
from abc import ABC, abstractmethod
import random
from typing import Any


class Monster(ABC):
    """Абстрактный класс чудовищ."""

    def __init__(self, game: Any) -> None:
        """Инициализация класса."""
        super().__init__()
        self.game = game
        self.game_stats = self.game.game_stats

    @abstractmethod
    def spawn(self) -> None:
        """Появление чудовища."""
        print("Перед вами появилось чудовище!")

    @abstractmethod
    def attack(self) -> None:
        """Функция атаки чудовища."""
        print(
            f"Противник атакует! Урон вашему здоровью составляет {self.game_stats.monster_power} единиц."
        )

    @abstractmethod
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
        """Инициализация класса."""
        self.game = game
        super().__init__(self.game)
        self.game_stats = self.game.game_stats
        self.power = power
        self.hp = hp

    def spawn(self) -> None:
        """Появление злого чародея."""
        self.game_stats.monster_type = "колдун"
        print(
            f"Перед вами возник злой чародей! Его мощь - {self.power}, а запас здоровья - {self.hp}."
        )
        self.game_stats.monster_power = self.power
        self.game_stats.monster_hp = self.hp
        self.game.hero.react()

    def attack(self) -> None:
        """Функция атаки чародея."""
        print("Злой чародей атакует!")
        self.game.hero.be_attacked()

    def be_attacked(self) -> None:
        """Функция реакции чародея на атаку героя."""
        updated_hp = self.game_stats.monster_hp - self.game_stats.hero_power
        self.game_stats.monster_hp = updated_hp
        if self.game_stats.monster_hp <= 0:
            print("Победа! Чародей пал! Движемся дальше...")
            sleep(1)
            self.game.run_game()
        print(
            f"Злой колдун морщится от боли! Он потерял {self.game_stats.hero_power} здоровья."
            f"Здоровья осталось {self.game_stats.monster_hp} ."
        )
        self.attack()


class ArcherSkeleton(Monster):
    """Класс скелета-лучника."""

    def __init__(self, game: Any, power: int, hp: int) -> None:
        """Инициализация класса."""
        self.game = game
        super().__init__(self.game)
        self.game_stats = self.game.game_stats
        self.power = power
        self.hp = hp

    def spawn(self) -> None:
        """Появление скелета-лучника."""
        self.game_stats.monster_type = "скелет"
        print(
            f"Вам на пути попался скелет-лучник! Его мощь - {self.power}, а запас здоровья - {self.hp}."
        )
        self.game_stats.monster_power = self.power
        self.game_stats.monster_hp = self.hp
        self.game.hero.react()

    def attack(self) -> None:
        """Функция атаки скелета-лучника."""
        print("Скелет стреляет в вас из лука!")
        self.game.hero.be_attacked()

    def be_attacked(self) -> None:
        """Функция реакции скелета-лучника на атаку героя."""
        updated_hp = self.game_stats.monster_hp - self.game_stats.hero_power
        self.game_stats.monster_hp = updated_hp
        if self.game_stats.monster_hp <= 0:
            print("Победа! Скелет развалился на части! Движемся дальше...")
            sleep(1)
            self.game.run_game()
        print(
            f"Из скелета вылетают кости! Он потерял {self.game_stats.hero_power} здоровья."
            f"Здоровья осталось {self.game_stats.monster_hp} ."
        )
        self.attack()


class SwordsmanGoblin(Monster):
    """Класс гоблина с мечом."""

    def __init__(self, game: Any, power: int, hp: int) -> None:
        """Инициализация класса."""
        self.game = game
        super().__init__(self.game)
        self.game_stats = self.game.game_stats
        self.power = power
        self.hp = hp

    def spawn(self) -> None:
        """Появление гоблина."""
        self.game_stats.monster_type = "гоблин"
        print(
            f"Внезапно на вас выбегает гоблин с мечом! Его мощь - {self.power}, а запас здоровья - {self.hp}."
        )
        self.game_stats.monster_power = self.power
        self.game_stats.monster_hp = self.hp
        self.game.hero.react()

    def attack(self) -> None:
        """Функция атаки гоблина."""
        print("Гоблин несется на вас с мечом!")
        self.game.hero.be_attacked()

    def be_attacked(self) -> None:
        """Функция реакции гоблина на атаку героя."""
        updated_hp = self.game_stats.monster_hp - self.game_stats.hero_power
        self.game_stats.monster_hp = updated_hp
        if self.game_stats.monster_hp <= 0:
            print("Победа! Гоблин повержен! Движемся дальше...")
            sleep(1)
            self.game.run_game()
        print(
            f"Гоблин ранен! Он потерял {self.game_stats.hero_power} здоровья."
            f"Здоровья осталось {self.game_stats.monster_hp}. "
        )
        self.attack()


class MonsterFactory(ABC):
    """Абстрактная фабрика игрового противника."""

    def __init__(self, game: Any) -> None:
        """Инициализация класса."""
        self.game = game
        super().__init__()
        self.create_monster()

    @abstractmethod
    def create_monster(self) -> object:
        """Создание чудовища."""
        pass


class WizardFactory(MonsterFactory):
    """Фабрика по производству злых чародеев."""

    def __init__(self, game: Any) -> None:
        """Инициализация класса."""
        self.game = game
        super().__init__(self.game)
        self.game_stats = self.game.game_stats

    def create_monster(self) -> None:
        """Создание злого чародея."""
        power = random.randint(6, 25)
        hp = random.randint(10, 40)
        wizard = EvilWizard(self.game, power, hp)
        wizard.spawn()


class SkeletonFactory(MonsterFactory):
    """Фабрика по производству скелетов-лучников."""

    def __init__(self, game: Any) -> None:
        """Инициализация класса."""
        self.game = game
        super().__init__(self.game)
        self.game_stats = self.game.game_stats

    def create_monster(self) -> None:
        """Создание скелетов-лучников."""
        power = random.randint(2, 15)
        hp = random.randint(5, 25)
        skeleton = ArcherSkeleton(self.game, power, hp)
        skeleton.spawn()


class GoblinFactory(MonsterFactory):
    """Фабрика по производству гоблинов с мечом."""

    def __init__(self, game: Any) -> None:
        """Инициализация класса."""
        self.game = game
        super().__init__(self.game)
        self.game_stats = self.game.game_stats

    def create_monster(self) -> None:
        """Создание гоблинов."""
        power = random.randint(4, 20)
        hp = random.randint(5, 35)
        goblin = SwordsmanGoblin(self.game, power, hp)
        goblin.spawn()
