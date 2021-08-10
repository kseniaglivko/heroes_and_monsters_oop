"""
Фабрика по производству героев.
"""

from abc import ABC, abstractmethod
import random
from time import sleep


class Item(ABC):
    """Абстрактный класс игровых предметов."""

    def __init__(self, game):
        super().__init__()
        self.game = game

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
        spawner = item_spawner[spawner_type](self.game)
        item = spawner.create_item()
        item.spawn()


class Totem(Item):
    """Класс тотема."""

    def __init__(self, game):
        self.game = game
        super().__init__(self.game)
        self.game_stats = self.game.game_stats

    def spawn(self):
        print(
            "Вы обнаружили волшебный тотем! Вселенная запомнила это мгновение, и вы сможете вернутся сюда!"
        )

    def totem_taken(self):
        self.game_stats.update_game_stats("totem", 1)
        self.game_stats.save_game()
        sleep(1)


class Apple(Item):
    """Класс целебного яблочка."""

    def __init__(self, game, apple_hp):
        self.game = game
        super().__init__(self.game)
        self.game_stats = self.game.game_stats
        self.apple_hp = apple_hp

    def spawn(self):
        print(
            f"Вы нашли целебное яблоко! Съев его, вы восстановили {self.apple_hp} единиц здоровья."
        )
        hp = self.game_stats.get_game_stats("hero", "hp")
        updated_hp = hp + self.apple_hp
        self.game_stats.update_game_stats("hero", updated_hp, "hp")
        sleep(1)


class Sword(Item):
    """Класс меча."""

    def __init__(self, game, power):
        self.game = game
        super().__init__(self.game)
        self.game_stats = self.game.game_stats
        self.power = power

    def spawn(self):
        print(f"Вы нашли новый меч! Его мощь составляет {self.power} единиц.")


class Spell(Item):
    """Класс заклинания."""

    def __init__(self, game, spell_type, power):
        self.game = game
        super().__init__(self.game)
        self.game_stats = self.game.game_stats
        self.spell_type = spell_type
        self.power = power

    def spawn(self):
        print(
            f"Вы нашли свиток, это {self.spell_type}! Его мощь составляет{self.power}."
        )


class Bow(Item):
    """Класс лука."""

    def __init__(self, game):
        self.game = game
        super().__init__(self.game)

    def spawn(self):
        print("Вы нашли новый лук!")


class Arrows(Item):
    """Класс стрел."""

    def __init__(self, game, quantity, power):
        self.game = game
        super().__init__(self.game)
        self.quantity = quantity
        self.power = power

    def spawn(self):
        print(
            f"Вы нашли колчан со стрелами! Количество стрел в колчане: {self.quantity}, "
            f"а мощь одной стрелы составляет {self.power}."
        )


class ItemFactory(ABC):
    """Абстрактная фабрика игровых предметов."""

    def __init__(self, game):
        self.game = game
        super().__init__(self.game)

    @abstractmethod
    def create_item(self):
        pass


class TotemFactory(ItemFactory):
    """Фабрика по производству тотемов."""

    def __init__(self, game):
        self.game = game
        super().__init__(self.game)

    def create_item(self):
        return Totem(self.game)


class AppleFactory(ItemFactory):
    """Фабрика по производству целебных яблочек."""

    def __init__(self, game):
        self.game = game
        super().__init__(self.game)

    def create_item(self):
        apple_hp = random.randint(2, 4)
        return Apple(self.game, apple_hp)


class SwordFactory(ItemFactory):
    """Фабрика по производству мечей."""

    def __init__(self, game):
        self.game = game
        super().__init__(self.game)

    def create_item(self):
        power = random.randint(4, 20)
        return Sword(self.game, power)


class SpellFactory(ItemFactory):
    """Фабрика по производству заклинаний."""

    def __init__(self, game):
        self.game = game
        super().__init__(self.game)
        self.game_stats = self.game.game_stats

    def create_item(self):
        spells = self.game_stats.get_game_stats("spell", "type")
        power = random.randint(6, 25)
        spell_type = random.choice(spells)
        return Spell(self.game, spell_type, power)


class BowFactory(ItemFactory):
    """Фабрика по производству луков."""

    def __init__(self, game):
        self.game = game
        super().__init__(self.game)

    def create_item(self):
        return Bow(self.game)


class ArrowsFactory(ItemFactory):
    """Фабрика по производству стрел."""

    def __init__(self, game):
        self.game = game
        super().__init__(self.game)

    def create_item(self):
        quantity = random.randint(1, 10)
        power = random.randint(5, 12)
        return Arrows(self.game, quantity, power)
