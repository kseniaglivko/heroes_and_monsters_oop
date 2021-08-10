"""
Модуль, собирающий статистику о процессе игры. С помощью него будет реализовано сохранение игры.
"""

import json
import jsonschema
from statistics_schema import statistics_schema


# Дефолтные параметры игровой статистики. С ними начинаем игру.
default_parameters = {
    "monster_counter": 0,
    "totem": 0,
    "arrows": {"name": "колчан со стрелами", "quantity": 0, "power": 0},
    "bow": {"name": "лук", "quantity": 0},
    "sword": {"name": "меч", "quantity": 1, "power": 10},
    "spell": {"type": "", "quantity": 0, "power": 0},
    "hero": {"type": "", "power": 10, "hp": 15},
    "monster": {"type": "", "power": "", "hp": ""},
}


class GameStats:
    def __init__(self, game):
        self.game = game

    @staticmethod
    def reset_stats():
        """Функция, обнуляющая игровую статистику."""
        with open("game_process_info.json", "w") as file:
            json.dump(default_parameters, file)

    @staticmethod
    def get_game_stats(from_, what=None):
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
    def update_game_stats(from_, value, what=None):
        """Функция, обновляющая игровую статистику."""
        file = open("game_process_info.json", "w+")
        try:
            game_info = json.load(file)
            game_info[from_][what] = value
            return json.dump(game_info, file)
        except json.decoder.JSONDecodeError:
            raise Exception(
                "Ошибка инициализации игровой статистики. Пожалуйста, начните игру заново."
            )

    @staticmethod
    def save_game():
        """Функция,сохраняющая игру."""
        with open("game_process_info.json", "r") as from_:
            with open("saved_game.json", "w+") as to:
                to.write(from_.read())

    def load_game(self):
        """Функция, загружающая сохраненную игру."""
        with open("saved_game.json", "r") as from_:
            with open("game_process_info.json", "w+") as to:
                to.write(from_.read())
                self.update_game_stats("totem", 0)
                self.game.run_game()

    @staticmethod
    def choose_hero(self):
        hero_input = input(
            "Пожалуйста, выберите класс для вашего героя - Маг, Мечник или Лучник): "
        ).capitalize()
        try:
            jsonschema.validate({"hero[type]": "hero_input"}, statistics_schema)
        except jsonschema.exceptions.ValidationError:
            print("Пожалуйста, выберите один из предложенные классов.")
            self.choose_hero()
        self.update_game_stats("hero", hero_input, "type")
