"""
Модуль, собирающий статистику о процессе игры. С помощью него будет реализовано сохранение игры.
"""

import os
import json
import jsonschema
from statistics_schema import statistics_schema


def get_game_stats(from_, what=None):
    with open("game_process_info.json", "r") as file:
        try:
            game_info = json.load(file)
            return game_info[from_][what]
        except json.decoder.JSONDecodeError:
            os.remove("game_process_info.json")
            raise Exception(
                "Ошибка инициализации игровой статистики. Пожалуйста, начните игру заново."
            )


def update_game_stats(from_, value, what=None):
    file = open("game_process_info.json", "w+")
    try:
        game_info = json.load(file)
        game_info[from_][what] = value
        return json.dump(game_info, file)
    except json.decoder.JSONDecodeError:
        os.remove("game_process_info.json")
        raise Exception(
            "Ошибка инициализации игровой статистики. Пожалуйста, начните игру заново."
        )


default_parameters = {
    "monster_counter": 0,
    "hero": {"type": "", "power": 10, "hp": 15,},
    "monster": {"type": "", "power": "", "hp": "",},
    "inventory": "[{'Меч': 10}]",
}


def reset_stats():
    try:
        os.remove("game_process_info.json")
        json.dumps(default_parameters)
    except FileNotFoundError:
        json.dumps(default_parameters)


class GameStats:
    def __init__(self, game):
        self.game = game
        self.choose_hero()

    def choose_hero(self):
        hero_input = input(
            "Пожалуйста, выберите класс для вашего героя (Маг/Мечник/Лучник): "
        ).capitalize()
        try:
            jsonschema.validate({"hero[type]": "hero_input"}, statistics_schema)
        except jsonschema.exceptions.ValidationError:
            print(
                "Пожалуйста, выберите один из предложенные классов (Маг/Мечник/Лучник)."
            )
            self.choose_hero()
        update_game_stats("hero", "type", hero_input)
