"""
Модуль, собирающий статистику о процессе игры. С помощью него будет реализовано сохранение игры.
"""


class GameStats:
    def __init__(self, game):
        self.reset_stats()

        # Начинаем игру в неактивном состоянии.
        self.game_active = False

        # Пишем игровую статистику.
        with open("game_process_info.txt", "r+") as file:
            pass
            # hero_hp, monsters_killed, hero_power, inventory = file.read()
            # if {...} == "":
            #   {...} == 0

        # self.{...} = int{...}

    def reset_stats(self):
        pass
        # self.{...} = self.{...}.self{...}
        # self.monsters_killed = 0
        # self.hero_hp = {...}
        # ...

    def hero_attack_power(self, power):
        pass

    def fill_inventory(self, item):
        pass

    def monster_counter(self):
        pass
