"""Модуль, собирающий статистику о процессе игры. С помощью него будет реализовано сохранение игры."""

import json
from typing import Any

# Дефолтные параметры игровой статистики. С ними начинаем игру.
default_parameters = {
    "monster_counter": 0,
    "totem": 0,
    "arrows": {"quantity": 0, "power": 0},
    "bow": 0,
    "sword": {"quantity": 1, "power": 10},
    "spell": {"type": "", "quantity": 0, "power": 0},
    "hero": {"type": "", "power": 10, "hp": 15},
    "monster": {"power": "", "hp": ""},
}


class GameStats:
    """Класс игровой статистики."""

    def __init__(self, game: Any) -> None:
        """Инициализация класса."""
        self.game = game

    @staticmethod
    def reset_stats() -> None:
        """Функция, обнуляющая игровую статистику."""
        with open("game_process_info.json", "w") as file:
            json.dumps(default_parameters)

    @staticmethod
    def get_game_stats(from_: str, what: str = None) -> str:
        """Функция, выводящая игровую статистику."""
        with open("game_process_info.json", "r") as file:
            try:
                game_info = json.load(file)
                return game_info[from_][what]
            except json.decoder.JSONDecodeError:
                raise Exception(
                    "Ошибка инициализации игровой статистики. Пожалуйста, начните игру заново."
                )

    @staticmethod
    def update_game_stats(from_: str, value: Any, what: str = None) -> None:
        """Функция, обновляющая игровую статистику."""
        with open("game_process_info.json", "r") as file:
            try:
                game_info = json.load(file)
                game_info[from_][what] = value
                with open("game_process_info.json", "w") as f:
                    json.dump(game_info, f)
            except json.decoder.JSONDecodeError:
                raise Exception(
                    "Ошибка инициализации игровой статистики. Пожалуйста, начните игру заново."
                )

    @staticmethod
    def save_game() -> None:
        """Функция,сохраняющая игру."""
        with open("game_process_info.json", "r") as from_:
            with open("saved_game.json", "w+") as to:
                to.write(from_.read())

    def load_game(self) -> None:
        """Функция, загружающая сохраненную игру."""
        with open("saved_game.json", "r") as from_:
            with open("game_process_info.json", "w+") as to:
                to.write(from_.read())
                self.update_game_stats("totem", 0)
                self.game.run_game()

    def choose_hero(self) -> None:
        """Функция, реализующая выбор персонажа."""
        hero_input = (input(
            "Пожалуйста, выберите класс для вашего героя - Маг, Мечник или Лучник): "
        )).lower()
        if hero_input == "маг":
            self.update_game_stats("hero", "маг", "type")
        if hero_input == "мечник":
            self.update_game_stats("hero", "мечник", "type")
        if hero_input == "лучник":
            self.update_game_stats("hero", "лучник", "type")
        else:
            print("Пожалуйста, выберите один из предложенных классов.")
            self.choose_hero()

    def check_hero_type(self) -> Any:
        """Проверка типа героя и начисление ему бонусов к атаке в зависимости от типа найденного оружия."""
        hero_type = self.get_game_stats("hero", "type")
        if hero_type == "мечник":
            if self.game.spawner_type == "sword":
                print(
                    "Ура! Поскольку вы - могучий мечник, то бонус к силе вашего меча +3!"
                )
                sword_power = int(self.get_game_stats("sword", "power"))
                updated_power = sword_power + 3
                self.update_game_stats("sword", updated_power, "hp")
            else:
                pass
        if hero_type == "лучник":
            if self.game.spawner_type == "arrows":
                print(
                    "Ура! Поскольку вы - отменный лучник, то бонус к силе ваших стрел +3!"
                )
                arrows_power = int(self.get_game_stats("arrows", "power"))
                updated_power = arrows_power + 3
                self.update_game_stats("arrows", updated_power, "hp")
            else:
                pass
        if hero_type == "маг":
            if self.game.spawner_type == "spell":
                print(
                    "Ура! Поскольку вы - великий маг, то бонус к силе вашего заклинания +3!"
                )
                spell_power = int(self.get_game_stats("spell", "power"))
                updated_power = spell_power + 3
                self.update_game_stats("spell", updated_power, "hp")
            else:
                pass
        pass
