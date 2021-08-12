"""Фабрика по производству героев."""

from time import sleep
from typing import Any


class Hero:
    """Класс героя."""

    def __init__(self, game: Any) -> None:
        """Инициализация класса."""
        self.game = game
        self.game_stats = self.game.game_stats
        self.arrows = self.game.arrows
        self.bow = self.game.bow
        self.spell = self.game.spell
        self.totem = self.game.totem
        self.sword = self.game.sword

    def react(self) -> None:
        """Реакция героя на событие."""
        if self.game.random_function == self.game.enemy_spawner:
            reaction = input("Нажмите 1, чтобы атаковать, 2 - чтобы убежать: ")
            self.activate_reaction_to_monster(reaction)
        if self.game.random_function == self.game.object_spawner:
            if self.game_stats.item_type == "яблоко":
                pass
            reaction = input(
                "Нажмите 1, чтобы подобрать находку, 2 - чтобы пройти мимо: "
            )
            self.activate_reaction_to_item(reaction)
        pass

    def reaction_after_death(self) -> None:
        """Выбор действия после смерти героя, у которого есть тотем, - загрузить игру или выйти из игры."""
        reaction = input(
            "Нажмите 1, чтобы загрузить сохраненную игру, 2 - чтобы выйти из игры: "
        )
        if reaction == "1":
            self.game_stats.load_game()
        elif reaction == "2":
            print("Пока! Увидимся еще!")
            exit()
        else:
            print("Неверный ввод!")
            self.reaction_after_death()

    def activate_reaction_to_item(self, reaction: str) -> None:
        """Функция, реализующая реакцию героя на игровой предмет."""
        if reaction == "1":
            self.take_item()
        elif reaction == "2":
            self.pass_by()
        else:
            print("Неверный ввод!")
            self.react()

    def activate_reaction_to_monster(self, reaction: str) -> None:
        """Функция, реализующая реакцию героя на появление чудовища."""
        if reaction == "1":
            self.choose_weapon()
        elif reaction == "2":
            self.run()
        else:
            print("Неверный ввод!")
            self.react()

    def take_item(self) -> None:
        """Взять игровой предмет в инвентарь."""
        if self.game_stats.item_type == "тотем":
            self.totem.be_taken()
        if self.game_stats.item_type == "лук":
            self.bow.be_taken()
        if self.game_stats.item_type == "стрелы":
            self.arrows.be_taken()
        if self.game_stats.item_type == "меч":
            self.sword.be_taken()
        if self.game_stats.item_type == "заклинание":
            self.spell.be_taken()

    def pass_by(self) -> None:
        """Пройти мимо игрового предмета."""
        print("Вы прошли мимо находки. Ну что тоже, идем дальше...")
        sleep(1)
        self.game.run_game()

    def choose_weapon(self) -> None:
        """Выбрать оружие для атаки."""
        print(
            "Выберите оружие для атаки. Вот ваш инвентарь:"
            f"\nмеч с силой атаки {self.game_stats.sword_power}"
        )
        if self.game_stats.arrows_quantity != 0 and self.game_stats.bow != 0:
            print(
                f"лук и стрелы в количестве {self.game_stats.arrows_quantity}, "
                f"мощь - {self.game_stats.arrows_power}"
            )
        if self.game_stats.spell_quantity == 1:
            print(
                f"{self.game_stats.spell_type} мощью {self.game_stats.spell_power}"
            )
        choice = input("1 - меч, 2 - лук и стрелы, 3 - заклинание: ")
        if choice == "1":
            print("Вы выбрали меч!")
            self.game_stats.hero_power = self.game_stats.sword_power
        if choice == "2":
            if self.game_stats.bow != 0 and self.game_stats.arrows_quantity != 0:
                print("Вы выбрали лук и стрелы!")
                self.game_stats.hero_power = self.game_stats.arrows_power
            else:
                print("У вас нет лука и/или стрел. Выберите другое оружие.")
                self.choose_weapon()
        if choice == "3":
            if self.game_stats.spell_quantity != 0:
                print("Вы выбрали магию!")
                self.game_stats.hero_power = self.game_stats.spell_power
            else:
                print("Вы не знаете ни одного заклинания. Выберите другое оружие.")
                self.choose_weapon()
        self.attack()

    def attack(self) -> None:
        """Функция, реализующая атаку героя."""
        print(f"Вы атакуете противника и наносите ему урон {self.game_stats.hero_power}.")
        if self.game_stats.monster_type == "колдун":
            self.game.wizard.be_attacked()
        if self.game_stats.monster_type == "гоблин":
            self.game.goblin.be_attacked()
        if self.game_stats.monster_type == "скелет":
            self.game.skeleton.be_attacked()
        pass

    def be_attacked(self) -> None:
        """Функция, реализующая нанесение ущерба герою после атаки монстра."""
        updated_hp = self.game_stats.hero_hp - self.game_stats.monster_power
        self.game_stats.hero_hp = updated_hp
        if self.game_stats.hero_hp <= 0:
            if self.game_stats.totem == 1:
                print(
                    "Вы погибли, но вас может спасти волшебный тотем! Загрузить сохраненную игру?"
                )
                self.reaction_after_death()
            else:
                print("Поражение! Вы умерли :(")
                exit()
        print(
            f"Вы ранены! Вы потеряли {self.game_stats.monster_power} здоровья."
            f"Здоровья осталось {self.game_stats.hero_hp}. "
        )
        self.choose_weapon()

    def run(self) -> None:
        """Побег героя от чудовища."""
        print("Вы сбежали от чудовища! Отдыхаем и продолжаем путь...")
        sleep(1)
        self.game.run_game()
