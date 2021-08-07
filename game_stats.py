"""
Модуль, собирающий статистику о процессе игры. С помощью него будет реализовано сохранение игры.
"""

import os
import json
from utils import getter, setter
from statisctics_schema import statistics_schema


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

    @getter
    def get_hero_power(self):
        pass

    @getter
    def get_hero_hp(self):
        pass

    @getter
    def get_monster_hp(self):
        pass

    @getter
    def get_monster_power(self):
        pass

    @setter
    def update_hero_hp(self):
        pass

    @setter
    def update_hero_power(self):
        pass

    @setter
    def update_monster_hp(self):
        pass

    @setter
    def fill_inventory(self, item):
        pass

    @getter
    def get_monster_counter(self):
        pass

    @setter
    def update_monster_counter(self):
        pass
