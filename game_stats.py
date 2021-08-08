"""
Модуль, собирающий статистику о процессе игры. С помощью него будет реализовано сохранение игры.
"""

import os
import json
import jsonschema
from statistics_schema import statistics_schema


# Дефолтные параметры игровой статистики. С ними начинаем игру.
default_parameters = {
    "monster_counter": 0,
    "hero": {"type": "", "power": 10, "hp": 15},
    "monster": {"type": "", "power": "", "hp": ""},
    "inventory": "[{'Меч': 10}]",
}


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


def reset_stats():
    """Функция, обнуляющая игровую статистику."""
    try:
        os.remove("game_process_info.json")
    except FileNotFoundError:
        pass
    json.dumps(default_parameters)


def choose_hero():
    hero_input = input(
        "Пожалуйста, выберите класс для вашего героя - Маг, Мечник или Лучник): "
    ).capitalize()
    try:
        jsonschema.validate({"hero[type]": "hero_input"}, statistics_schema)
    except jsonschema.exceptions.ValidationError:
        print("Пожалуйста, выберите один из предложенные классов.")
        choose_hero()
    update_game_stats("hero", hero_input, "type")
