"""
Фабрика по производству героев.
"""

from abc import ABC, abstractmethod
from time import sleep
from game_stats import GameStats


class Hero(ABC):
    """Абстрактный класс героя."""

    def __init__(self, game, hp, power, item):
        super().__init__()
        self.game = game
        self.hp = hp
        self.item = item
        self.power = power

    @abstractmethod
    def attack(self, power):
        # В дальнейшем планируется выводить информацию о оставшемся здоровье у противника.
        return f"Вы атаковали чудовище! Урон чудовищу составил {power}."

    def run(self):
        sleep(2)
        print("Вы успешно сбежали от чудовища! Отдыхаем и продолжаем путь...")
        self.game.run_game()

    def take_item(self):
        # inventory.add[...]/GameStats.fill_inventory()
        return "Вы взяли предмет! Теперь он добавлен в ваш инвентарь."

    @abstractmethod
    def choose_weapon(self):
        pass


class Mage(Hero):
    """Класс героя-мага."""

    def attack(self, power):
        pass

    def choose_weapon(self):
        pass


class Archer(Hero):
    """Класс героя-лучника."""

    def attack(self, power):
        pass

    def choose_weapon(self):
        pass


class Swordsman(Hero):
    """Класс героя-мечника."""

    def attack(self, power):
        pass

    def choose_weapon(self):
        pass
