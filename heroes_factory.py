"""
Фабрика по производству героев.
"""

from abc import ABC, abstractmethod


class Hero(ABC):
    """Абстрактный класс героя."""

    def __init__(self, power):
        super().__init__()
        self.attack_power = power

    @abstractmethod
    def attack(self, power):
        # В дальнейшем планируется выводить информацию о оставшемся здоровье у противника.
        return f"Вы атаковали чудовище! Урон чудовищу составил {power}."
