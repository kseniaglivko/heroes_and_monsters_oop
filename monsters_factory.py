"""
Фабрика по производству героев.
"""

from abc import ABC, abstractmethod
from time import sleep
from game_stats import GameStats
from game_class import Game
from heroes_factory import Hero


class Monster(ABC):
    """Абстрактный класс чудовищ."""

    def __init__(self, game, hp, power):
        super().__init__()
        self.game = game
        self.monster_hp = hp
        self.monster_power = power
        self.game_stats = GameStats(self.game)

    @abstractmethod
    def spawn(self, power):
        print(f"Перед вами появилось чудовище!")
        self.gamer_reaction_to_monster()

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

    @abstractmethod
    def attack(self, power):
        # В дальнейшем планируется выводить информацию о оставшемся здоровье у противника.
        return f"Чудовище атаковало вас! Урон вашему здоровью составляет {power}."

    @abstractmethod
    def run(self):
        return "Чудовище убежало от вас! Отправляемся дальше."


class EvilWizard(Monster):
    """Класс злого чародея."""

    def attack(self, power):
        return f"Злой чародей атакует! Сила атаки - {power}."

    def run(self):
        return "Злой чародей убегает от вас!"


class ArcherSkeleton(Monster):
    """Класс скелета-лучника."""

    def attack(self, power):
        return f"Скелет стреляет в вас из лука! Сила атаки - {power}."

    def run(self):
        return "Скелет убегает от вас!"


class SwordsmanGoblin(Monster):
    """Класс гоблина с мечом."""

    def attack(self, power):
        return f"Гоблин несется на вас с мечом! Сила атаки - {power}."

    def run(self):
        return "Гоблин убегает от вас!"


class MonsterFactory(ABC):
    """Абстрактная фабрика игрового противника."""

    @abstractmethod
    def create_enemy(self):
        pass


class WizardFactory(MonsterFactory):
    """Фабрика по производству злых чародеев."""

    def create_monter(self):
        return EvilWizard()


class SkeletonFactory(MonsterFactory):
    """Фабрика по производству скелетов-лучников."""

    def create_monster(self):
        return ArcherSkeleton()


class GoblinFactory(MonsterFactory):
    """Фабрика по производству гоблинов с мечом."""

    def create_monster(self):
        return SwordsmanGoblin()
