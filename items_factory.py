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

    @abstractmethod
    def be_taken(self):
        pass


class Totem(Item):
    """Класс тотема."""

    def __init__(self, game):
        self.game = game
        super().__init__(self.game)
        self.game_stats = self.game.game_stats

    def spawn(self):
        print(
            "Вы обнаружили волшебный тотем! С его помощью вы сможете сохраниться на настоящем моменте."
        )

    def be_taken(self):
        print(
            "Вы подобрали волшебный тотем! Вселенная запомнила это мгновение, и вы сможете вернутся сюда!"
        )
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

    def be_taken(self):
        pass


class Sword(Item):
    """Класс меча."""

    def __init__(self, game, power):
        self.game = game
        super().__init__(self.game)
        self.game_stats = self.game.game_stats
        self.power = power

    def spawn(self):
        print(f"Вы нашли новый меч! Его мощь составляет {self.power} единиц.")

    def be_taken(self):
        print("Поздравляем, теперь у вас новый меч!")
        self.game_stats.update_game_stats("sword", 1, "quantity")
        self.game_stats.update_game_stats("sword", {self.power}, "power")
        sleep(1)


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

    def be_taken(self):
        print("Поздравляем, теперь вы знаете новое заклинание!")
        self.game_stats.update_game_stats("spell", {self.spell_type}, "type")
        self.game_stats.update_game_stats("spell", 1, "quantity")
        self.game_stats.update_game_stats("spell", {self.power}, "power")
        sleep(1)


class Bow(Item):
    """Класс лука."""

    def __init__(self, game):
        self.game = game
        super().__init__(self.game)
        self.game_stats = self.game.game_stats

    def spawn(self):
        print("Вы нашли новый лук!")

    def be_taken(self):
        print("Поздравляем, теперь у вас новый лук!")
        self.game_stats.update_game_stats("bow", 1, "quantity")
        sleep(1)


class Arrows(Item):
    """Класс стрел."""

    def __init__(self, game, quantity, power):
        self.game = game
        super().__init__(self.game)
        self.quantity = quantity
        self.power = power
        self.game_stats = self.game.game_stats

    def spawn(self):
        print(
            f"Вы нашли колчан со стрелами! Количество стрел в колчане: {self.quantity}, "
            f"а мощь одной стрелы составляет {self.power}."
        )

    def be_taken(self):
        quantity = self.game_stats.get_game_stats("arrows", "quantity")
        power = self.game_stats.get_game_stats("arrows", "power")
        new_quantity = quantity + self.quantity
        new_power = (power + self.power) / 2
        print(f"Поздравляем, теперь количество ваших стрел: {self.quantity}!")
        self.game_stats.update_game_stats("arrows", {new_quantity}, "quantity")
        self.game_stats.update_game_stats("sword", {new_power}, "power")
        sleep(1)


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
