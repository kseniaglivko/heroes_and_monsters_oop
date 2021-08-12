"""Модуль, собирающий статистику о процессе игры. С помощью него будет реализовано сохранение игры."""

import json
from typing import Any


class GameStats:
    """Класс игровой статистики."""

    def __init__(self, game: Any) -> None:
        """Инициализация класса."""
        self.game = game
        self.monster_counter = 0
        self.totem = 0
        self.arrows_quantity = 0
        self.arrows_power = 0
        self.bow = 0
        self.sword_quantity = 1
        self.sword_power = 10
        self.spell_type = ""
        self.spell_quantity = 0
        self.spell_power = 0
        self.hero_type = ""
        self.hero_power = 10
        self.hero_hp = 15
        self.item_type = ""
        self.monster_type = ""
        self.monster_power = 0
        self.monster_hp = 0

    def reset_stats(self) -> None:
        """Функция, обнуляющая игровую статистику."""
        self.monster_counter = 0
        self.totem = 0
        self.arrows_quantity = 0
        self.arrows_power = 0
        self.bow = 0
        self.sword_quantity = 1
        self.sword_power = 10
        self.spell_type = ""
        self.spell_quantity = 0
        self.spell_power = 0
        self.hero_type = ""
        self.hero_power = 10
        self.hero_hp = 15
        self.item_type = ""
        self.monster_type = ""
        self.monster_power = 0
        self.monster_hp = 0

    def save_game(self) -> None:
        """Функция, сохраняющая игру."""
        self.save_monster_counter = self.monster_counter
        self.save_arrows_quantity = self.arrows_quantity
        self.save_arrows_power = self.arrows_power
        self.save_bow = self.bow
        self.save_sword_power = self.sword_power
        self.save_spell_type = self.spell_type
        self.save_spell_quantity = self.spell_quantity
        self.save_spell_power = self.spell_power
        self.save_hero_type = self.hero_type
        self.save_hero_power = self.hero_power
        self.save_hero_hp = self.hero_hp

    def load_game(self) -> None:
        """Функция, загружающая сохраненную игру."""
        self.monster_counter = self.save_monster_counter
        self.totem = 0
        self.arrows_quantity = self.save_arrows_quantity
        self.arrows_power = self.save_arrows_power
        self.bow = self.save_bow
        self.sword_quantity = 1
        self.sword_power = self.save_sword_power
        self.spell_type = self.save_spell_type
        self.spell_quantity = self.save_spell_quantity
        self.spell_power = self.save_spell_power
        self.hero_type = self.save_hero_type
        self.hero_power = self.save_hero_power
        self.hero_hp = self.save_hero_hp
        self.item_type = ""
        self.monster_type = ""
        self.monster_power = 0
        self.monster_hp = 0
        self.game.run_game()

    def choose_hero(self) -> None:
        """Функция, реализующая выбор персонажа."""
        print("Пожалуйста, выберите класс для вашего героя: 1 - Маг, 2 - Мечник, 3 - Лучник. Введите 1, 2 или 3.")
        hero_input = input()
        if hero_input == "1":
            self.hero_type = "маг"
        elif hero_input == "2":
            self.hero_type = "мечник"
        elif hero_input == "3":
            self.hero_type = "лучник"
        else:
            print("Пожалуйста, выберите один из предложенных классов.")
            self.choose_hero()
        self.game.run_game()

    def check_hero_type(self) -> Any:
        """Проверка типа героя и начисление ему бонусов к атаке в зависимости от типа найденного оружия."""
        if self.hero_type == "мечник":
            if self.item_type == "меч":
                print(
                    "Ура! Поскольку вы - могучий мечник, то бонус к силе вашего меча +3!"
                )
                self.sword_power += 3
            else:
                pass
        if self.hero_type == "лучник":
            if self.item_type == "стрелы":
                print(
                    "Ура! Поскольку вы - отменный лучник, то бонус к силе ваших стрел +3!"
                )
                self.arrows_power += 3
            else:
                pass
        if self.hero_type == "маг":
            if self.item_type == "заклинание":
                print(
                    "Ура! Поскольку вы - великий маг, то бонус к силе вашего заклинания +3!"
                )
                self.spell_power += 3
            else:
                pass
        pass
