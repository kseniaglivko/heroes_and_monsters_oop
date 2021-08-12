"""Фабрика по производству героев."""

from time import sleep
from typing import Any


class Hero:
    """Класс героя."""

    def __init__(self, game: Any) -> None:
        """Инициализация класса."""
        self.game = game
        self.game_stats = self.game.game_stats
        self.item = self.game.item
        self.monster = self.game.monster

    def react(self) -> None:
        """Реакция героя на событие."""
        if self.game.random_function == self.monster.spawn:
            reaction = input("Нажмите 1, чтобы атаковать, 2 - чтобы убежать.")
            self.activate_reaction_to_item(int(reaction))
        if self.game.random_function == self.monster.spawn:
            reaction = input(
                "Нажмите 1, чтобы подобрать находку, 2 - чтобы пройти мимо."
            )
            self.activate_reaction_to_monster(int(reaction))
        pass

    def reaction_after_death(self) -> None:
        """Выбор действия после смерти героя, у которого есть тотем, - загрузить игру или выйти из игры."""
        reaction = input(
            "Нажмите 1, чтобы загрузить сохраненную игру, 2 - чтобы выйти из игры."
        )
        if reaction == "1":
            self.game_stats.load_game()
        if reaction == "2":
            print("Пока! Увидимся еще!")
            exit()
        else:
            print("Неверный ввод!")
            self.reaction_after_death()

    def activate_reaction_to_item(self, reaction: int) -> None:
        """Функция, реализующая реакцию героя на игровой предмет."""
        if reaction == "1":
            self.take_item()
        if reaction == "2":
            self.pass_by()
        else:
            print("Неверный ввод!")
            self.activate_reaction_to_item(reaction)

    def activate_reaction_to_monster(self, reaction: int) -> None:
        """Функция, реализующая реакцию героя на появление чудовища."""
        if reaction == "1":
            self.choose_weapon()
        if reaction == "2":
            self.run()
        else:
            print("Неверный ввод!")
            self.activate_reaction_to_monster(reaction)

    def take_item(self) -> None:
        """Взять игровой предмет в инвентарь."""
        self.item.be_taken()

    def pass_by(self) -> None:
        """Пройти мимо игрового предмета."""
        print("Вы прошли мимо находки. Ну что тоже, идем дальше...")
        sleep(1)
        self.game.run_game()

    def choose_weapon(self) -> None:
        """Выбрать оружие для атаки."""
        print("Выберите оружие для атаки:")
        bow = int(self.game_stats.get_game_stats("bow"))
        arrows_quantity = int(self.game_stats.get_game_stats("arrows", "quantity"))
        arrows_power = int(self.game_stats.get_game_stats("arrows", "power"))
        sword_power = int(self.game_stats.get_game_stats("sword", "power"))
        spell_quantity = int(self.game_stats.get_game_stats("spell", "quantity"))
        spell_power = int(self.game_stats.get_game_stats("spell", "power"))
        spell_type = self.game_stats.get_game_stats("spell", "type")
        print("Выберите оружие для атаки. Вот ваш инвентарь:"
              f"\nМ - меч с силой атаки {sword_power}")
        if arrows_quantity != 0 and bow == 1:
            print(f"\nЛ - лук - {bow}."
                  f"\nстрелы в количестве {arrows_quantity}, мощь - {arrows_power}")
        if spell_quantity == 1:
            print(f"З - {spell_type} мощью {spell_power}")
        choice = input("Введите букву-индикатор оружия (М/Л/З): ").lower()
        if choice == "м":
            print("Вы выбрали меч!")
            sword_power = int(self.game_stats.get_game_stats("sword", "power"))
            self.game_stats.update_game_stats("hero", sword_power, "power")
        if choice == "л":
            print("Вы выбрали лук и стрелы!")
            arrows_power = int(self.game_stats.get_game_stats("arrows", "power"))
            self.game_stats.update_game_stats("hero", arrows_power, "power")
        if choice == "м":
            print("Вы выбрали магию!")
            spell_power = int(self.game_stats.get_game_stats("spell", "power"))
            self.game_stats.update_game_stats("hero", spell_power, "power")

        self.attack()

    def attack(self) -> None:
        """Функция, реализующая атаку героя."""
        power = int(self.game_stats.get_game_stats("hero", "power"))
        print(f"Вы атакуете противника и напасите ему урон {power}.")
        self.monster.be_attacked()

    def be_attacked(self) -> None:
        """Функция, реализующая нанесение ущерба герою после атаки монстра."""
        monster_attack = int(self.game_stats.get_game_stats("monster", "power"))
        hero_hp = int(self.game_stats.get_game_stats("hero", "hp"))
        updated_hp = hero_hp - monster_attack
        self.game_stats.update_game_stats("hero", updated_hp, "hp")
        if hero_hp <= 0:
            totem = int(self.game_stats.get_game_stats("totem", "quantity"))
            if totem == 1:
                print(
                    "Вы погибли, но вас может спасти волшебный тотем! Загрузить сохраненную игру?"
                )
                self.reaction_after_death()
        print(
            f"Вы ранены! Вы потеряли {monster_attack} здоровья."
            f"Здоровья осталось {updated_hp}. "
        )
        self.choose_weapon()

    def run(self) -> None:
        """Побег героя от чудовища."""
        print("Вы сбежали от чудовища! Отдыхаем и продолжаем путь...")
        sleep(1)
        self.game.run_game()
