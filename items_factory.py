"""Фабрика по производству игровых предметов."""

import random
from abc import abstractmethod, ABC
from typing import Any


class Item(ABC):
    """Абстрактный класс игровых предметов."""

    def __init__(self, game: Any) -> None:
        """Инициализация класса."""
        super().__init__()
        self.game = game

    @abstractmethod
    def spawn(self) -> None:
        """"Появление игрового объекта."""
        print("Перед вами появился игровой объект!")

    @abstractmethod
    def be_taken(self) -> None:
        """Функция, регулирующая последствия того, что игрок взял игровой предмет."""
        print("Вы взяли игровой предмет!")


class Totem(Item):
    """Класс тотема."""

    def __init__(self, game: Any) -> None:
        """Инициализация класса."""
        self.game = game
        super().__init__(self.game)
        self.game_stats = self.game.game_stats

    def spawn(self) -> None:
        """Появление тотема."""
        self.game_stats.item_type = "тотем"
        print(
            "Вы обнаружили волшебный тотем! С его помощью вы сможете сохраниться на настоящем моменте."
        )
        self.game.hero.react()

    def be_taken(self) -> None:
        """Сохранение игры по поднятию тотема."""
        print(
            "Вы подобрали волшебный тотем! Вселенная запомнила это мгновение, и вы сможете вернутся сюда!"
        )
        self.game_stats.totem = 1
        self.game_stats.save_game()
        self.game.run_game()


class Apple(Item):
    """Класс целебного яблочка."""

    def __init__(self, game: Any, apple_hp: int) -> None:
        """Инициализация класса."""
        self.game = game
        super().__init__(self.game)
        self.game_stats = self.game.game_stats
        self.apple_hp = apple_hp

    def spawn(self) -> None:
        """Появление целебного яблока."""
        self.game_stats.item_type = "яблоко"
        print(
            f"Вы нашли целебное яблоко! Съев его, вы восстановили {self.apple_hp} единиц здоровья."
        )
        self.game.run_game()

    # Активация яблока происходит в момент его появления, поскольку отказаться от него нельзя.
    def be_taken(self) -> None:
        """Активация целебного яблочка."""
        pass


class Sword(Item):
    """Класс меча."""

    def __init__(self, game: Any, power: int) -> None:
        """Инициализация класса."""
        self.game = game
        super().__init__(self.game)
        self.game_stats = self.game.game_stats
        self.power = power

    def spawn(self) -> None:
        """Появление меча."""
        self.game_stats.item_type = "меч"
        print(f"Вы нашли новый меч! Его мощь составляет {self.power} единиц.")
        self.game.hero.react()

    def be_taken(self) -> None:
        """Добавление меча в инвентарь."""
        print("Поздравляем, теперь у вас новый меч!")
        self.game_stats.sword_power = self.power
        self.game_stats.check_hero_type()
        self.game.run_game()


class Spell(Item):
    """Класс заклинания."""

    def __init__(self, game: Any, spell_type: str, power: int) -> None:
        """Инициализация класса."""
        self.game = game
        super().__init__(self.game)
        self.game_stats = self.game.game_stats
        self.spell_type = spell_type
        self.power = power

    def spawn(self) -> None:
        """Появление заклинания."""
        self.game_stats.item_type = "заклинание"
        print(
            f"Вы нашли свиток, это {self.spell_type}! Его мощь составляет {self.power}."
        )
        self.game.hero.react()

    def be_taken(self) -> None:
        """Добавление заклинания в инвентарь."""
        print("Поздравляем, теперь вы знаете новое заклинание!")
        self.game_stats.spell_type = self.spell_type
        self.game_stats.spell_quantity = 1
        self.game_stats.spell_power = self.power
        self.game_stats.check_hero_type()
        self.game.run_game()


class Bow(Item):
    """Класс лука."""

    def __init__(self, game: Any) -> None:
        """Инициализация класса."""
        self.game = game
        super().__init__(self.game)
        self.game_stats = self.game.game_stats

    def spawn(self) -> None:
        """Появление лука."""
        self.game_stats.item_type = "лук"
        print("Вы нашли новый лук!")
        self.game.hero.react()

    def be_taken(self) -> None:
        """Добавление лука в инвентарь."""
        print("Поздравляем, теперь у вас новый лук!")
        self.game_stats.bow = 1
        self.game.run_game()


class Arrows(Item):
    """Класс стрел."""

    def __init__(self, game: Any, quantity: int, power: int) -> None:
        """Инициализация класса."""
        self.game = game
        super().__init__(self.game)
        self.quantity = quantity
        self.power = power
        self.game_stats = self.game.game_stats

    def spawn(self) -> None:
        """Появление стрел."""
        self.game_stats.item_type = "стрелы"
        print(
            f"Вы нашли колчан со стрелами! Количество стрел в колчане: {self.quantity}, "
            f"а мощь одной стрелы составляет {self.power}."
        )
        self.game.hero.react()

    def be_taken(self) -> None:
        """Добавление стрел в инвентарь."""
        self.game_stats.arrows_quantity = self.game_stats.arrows_quantity + self.quantity
        new_power = (self.game_stats.arrows_power + self.power) / 2
        self.game_stats.arrows_power = new_power
        print(f"Поздравляем, теперь количество ваших стрел: {self.game_stats.arrows_quantity}!")
        self.game_stats.check_hero_type()
        self.game.run_game()


class ItemFactory(ABC):
    """Абстрактная фабрика игровых предметов."""

    def __init__(self, game: Any) -> None:
        """Инициализация класса."""
        self.game = game
        super().__init__()
        self.create_item()

    @abstractmethod
    def create_item(self) -> object:
        """Создание игрового объекта."""
        pass


class TotemFactory(ItemFactory):
    """Фабрика по производству тотемов."""

    def __init__(self, game: Any) -> None:
        """Инициализация класса."""
        self.game = game
        super().__init__(self.game)

    def create_item(self) -> None:
        """Создание тотема."""
        totem = Totem(self.game)
        totem.spawn()


class AppleFactory(ItemFactory):
    """Фабрика по производству целебных яблочек."""

    def __init__(self, game: Any) -> None:
        """Инициализация класса."""
        self.game = game
        super().__init__(self.game)

    def create_item(self) -> None:
        """Создание яблока."""
        apple_hp = random.randint(2, 4)
        apple = Apple(self.game, apple_hp)
        apple.spawn()


class SwordFactory(ItemFactory):
    """Фабрика по производству мечей."""

    def __init__(self, game: Any) -> None:
        """Инициализация класса."""
        self.game = game
        super().__init__(self.game)

    def create_item(self) -> None:
        """Создание меча."""
        power = random.randint(4, 20)
        sword = Sword(self.game, power)
        sword.spawn()


class SpellFactory(ItemFactory):
    """Фабрика по производству заклинаний."""

    def __init__(self, game: Any) -> None:
        """Инициализация класса."""
        self.game = game
        super().__init__(self.game)
        self.game_stats = self.game.game_stats

    def create_item(self) -> None:
        """Создание заклинания."""
        spells = [
            "заклинание школы магии огня 'Огненный шар'",
            "заклинание школы магии воды 'Ледяная стрела'",
            "заклинание школы магии земли 'Землетрясение'",
            "заклинание школы магии воздуха 'Молния'",
            "заклинание школы магии огня 'Огненный элементаль'",
            "заклинание школы магии воды 'Водный элементаль'",
            "заклинание школы магии земли 'Земляной элементаль'",
            "заклинание школы магии воздуха 'Воздушный элементаль'",
        ]
        power = random.randint(6, 25)
        spell_type = random.choice(spells)
        spell = Spell(self.game, spell_type, power)
        spell.spawn()


class BowFactory(ItemFactory):
    """Фабрика по производству луков."""

    def __init__(self, game: Any) -> None:
        """Инициализация класса."""
        self.game = game
        super().__init__(self.game)

    def create_item(self) -> None:
        """Создание лука."""
        bow = Bow(self.game)
        bow.spawn()


class ArrowsFactory(ItemFactory):
    """Фабрика по производству стрел."""

    def __init__(self, game: Any) -> None:
        """Инициализация класса."""
        self.game = game
        super().__init__(self.game)

    def create_item(self) -> None:
        """Создание стрел."""
        quantity = random.randint(1, 10)
        power = random.randint(5, 12)
        arrows = Arrows(self.game, quantity, power)
        arrows.spawn()
