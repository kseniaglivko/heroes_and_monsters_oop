"""
Модуль, собирающий статистику о процессе игры. С помощью него будет реализовано сохранение игры.
"""

import os
import json


class GameStats:
    def __init__(self, game):
        self.reset_stats()

        # Начинаем игру в неактивном состоянии.
        self.game_active = False

    def reset_stats(self):
        pass
        # self.{...} = self.{...}.self{...}
        # self.monsters_killed = 0
        # self.hero_hp = {...}
        # ...

    def get_game_stats(self, from_, what = None):
        with open("game_process_info.json", "r") as file:
            try:
                game_info = json.load(file)
                return game_info[from_][what]
            except json.decoder.JSONDecodeError:
                os.remove("game_process_info.json")
                raise Exception(
                    "Ошибка инициализации игровой статистики. Пожалуйста, начните игру заново."
                )

    def update_game_stats(self, from_, value, what = None):
        file = open("game_process_info.json", "a+")
        try:
            game_info = json.load(file)
            game_info[from_][what] = value
            return json.dump(game_info, file)
        except json.decoder.JSONDecodeError:
            os.remove("game_process_info.json")
            raise Exception(
                "Ошибка инициализации игровой статистики. Пожалуйста, начните игру заново."
            )