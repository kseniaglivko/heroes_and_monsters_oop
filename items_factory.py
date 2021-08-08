"""
Фабрика по производству героев.
"""

from abc import ABC, abstractmethod
import random
from time import sleep
from game_stats import GameStats
from heroes_factory import Hero


class Item(ABC):
    """Абстрактный класс игровых предметов."""

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.game_stats = GameStats(self.game)
        self.hero = Hero(self.game)

    @abstractmethod
    def spawn(self):
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
        spawner = item_spawner[spawner_type]()
        item = spawner.create_item()
        item.spawn(self)


class Totem(Item):
    """Класс тотема."""

    def spawn(self):
        power = None
        GameStats.game_active = True
        return f"Вы обнаружили волшебный тотем! Вселенная запомнила это мгновение, и вы сможете сюда вернуться!"
        self.hero.reaction_to_item()

class Apple(Item):
    """Класс целебного яблочка."""

    def spawn(self):
        return f"Вы нашли целебное яблоко! Съев его, вы восстановили {power} единиц здоровья."
        self.hero.reaction_to_item()

class Sword(Item):
    """Класс меча."""

    def spawn(self):
        return f"Вы нашли новый меч! Его мощь составляет {power} единиц."
        self.hero.reaction_to_item()

class Spell(Item):
    """Класс заклинания."""

    def spawn(self):
        spell_types = [
            "Вы нашли свиток с заклинанием школы магии огня 'Огненный шар'",
            "Вы нашли свиток с заклинанием школы магии воды 'Ледяная стрела'",
            "Вы нашли свиток с заклинанием школы магии земли 'Землетрясение'",
            "Вы нашли свиток с заклинанием школы магии воздуха 'Молния'",
            "Вы нашли свиток с заклинанием школы магии огня 'Огненный элементаль'",
            "Вы нашли свиток с заклинанием школы магии воды 'Водный элементаль'",
            "Вы нашли свиток с заклинанием школы магии земли 'Земляной элементаль'",
            "Вы нашли свиток с заклинанием школы магии воздуха 'Воздушный элементаль'",
        ]
        return f"{random.choice(spell_types)}! Вы наносите чудовищу урон в размере {power} единиц."


class Bow(Item):
    """Класс лука."""

    def spawn(self):
        return f"Вы новый лук! Его мощь составляет {power} единиц."
        self.hero.reaction_to_item()

class Arrows(Item):
    """Класс стрел."""

    def spawn(self):
        quantity = random.randint(1, 10)
        return f"Вы нашли колчан со стрелами! Количество стрел в колчане: {quantity}."
        self.hero.reaction_to_item()

class ItemFactory(ABC):
    """Абстрактная фабрика игровых предметов."""

    @abstractmethod
    def create_item(self):
        pass


class TotemFactory(ItemFactory):
    """Фабрика по производству тотемов."""

    def create_item(self):
        return Totem()


class AppleFactory(ItemFactory):
    """Фабрика по производству целебных яблочек."""

    def create_item(self):
        return Apple()


class SwordFactory(ItemFactory):
    """Фабрика по производству мечей."""

    def create_item(self):
        return Sword()


class SpellFactory(ItemFactory):
    """Фабрика по производству заклинаний."""

    def create_item(self):
        return Spell()


class BowFactory(ItemFactory):
    """Фабрика по производству луков."""

    def create_item(self):
        return Bow()


class ArrowsFactory(ItemFactory):
    """Фабрика по производству стрел."""

    def create_item(self):
        return Arrows()
