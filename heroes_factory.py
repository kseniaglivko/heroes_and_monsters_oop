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
        self.game_stats = GameStats()

    @abstractmethod
    def attack(self, power):
        def gamer_reaction_to_monster(self):
            """Функция, с помощью которой непосредственно реализуется бой с монстром."""
            reaction = input(
                "Начинается бой! Введите 1, чтобы атаковать чудовище, 2 - чтобы убежать: "
            )
            if reaction == "1":
                print("Атака!")
                sleep(0.5)
                updated_hp = self.game_stats.hero_hp - self.monster_power
                updated_monster_hp = self.monster_hp - self.game_stats.hero_power
                if updated_hp <= 0:
                    print("ПОРАЖЕНИЕ! Вы умерли :(")
                    exit()
                elif updated_monster_hp <= 0:
                    print(
                        "Вы победили чудовище! Отдохнув и восстановив силы, вы идете дальше..."
                    )
                    self.game_stats.monster_counter += 1
                    print(
                        f"Количество побежденных чудовищ: {self.game_stats.monster_counter}. Вы молодец!"
                    )
                    sleep(2)
                    self.game.run_game()
                else:
                    print(
                        f"Количество ваших жизней: {updated_hp}, количество жизней чудовища: {updated_monster_hp}."
                    )
                    self.gamer_reaction_to_monster(hp, monster_hp, monster_attack)
            elif reaction == "2":
                self.hero.run()
            else:
                print("Некорректный ввод!")
                self.gamer_reaction_to_monster(monster_hp, monster_attack)

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
