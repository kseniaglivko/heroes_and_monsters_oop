import random
from typing import Any

from objects.base_class import AbstractFactory
from objects.character_class import Warrior, Archer, Mage, MeleeMonster, ArcherMonster, MagicMonster


class HeroFactory(AbstractFactory):
    def create_hero(self, hero_class: str) -> Any:
        if hero_class not in ["warrior", "archer", "mage"]:
            raise ValueError("Invalid hero class")
        if hero_class == "warrior":
            return Warrior()
        elif hero_class == "archer":
            return Archer()
        elif hero_class == "mage":
            return Mage()

    def create_monster(self) -> Any:
        monster_type = random.choice(["melee", "archer", "magic"])
        if monster_type == "melee":
            return MeleeMonster()
        elif monster_type == "archer":
            return ArcherMonster()
        elif monster_type == "magic":
            return MagicMonster()
