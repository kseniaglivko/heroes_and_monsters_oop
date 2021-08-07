import os
import json


def getter(function):
    with open("game_process_info.json", "r") as file:
        try:
            game_info = json.load(file)
            function(game_info)
        except json.decoder.JSONDecodeError:
            os.remove("game_process_info.json")
            raise Exception(
                "Ошибка инициализации игровой статистики. Пожалуйста, начните игру заново."
            )


def setter(function):
    with open("game_process_info.json", "a+") as file:
        try:
            game_info = json.load(file)
            updates = function(game_info)
            json.dump(updates, game_info)
        except json.decoder.JSONDecodeError:
            os.remove("game_process_info.json")
            raise Exception(
                "Ошибка инициализации игровой статистики. Пожалуйста, начните игру заново."
            )
