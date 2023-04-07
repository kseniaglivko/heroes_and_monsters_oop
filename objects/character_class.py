class Character:
    def __init__(self, health: int, attack: int) -> None:
        self.health = health
        self.attack = attack

    def take_damage(self, damage: int) -> None:
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_dead(self) -> None:
        self.health == 0


class Hero(Character):
    def __init__(self, hero_class: str, health: int, attack: int) -> None:
        super().__init__(health, attack)
        self.hero_class = hero_class
        self.inventory = {"sword": True, "bow": False, "arrows": 0, "spellbook": False, "apple": 0, "totem": False}

    def pick_item(self, item: str) -> None:
        if item == "totem":
            self.inventory["totem"] = True
        elif item in self.inventory:
            self.inventory[item] += 1
        else:
            raise ValueError("Invalid item")


class Warrior(Hero):
    def __init__(self) -> None:
        super().__init__("warrior", 100, 15)


class Archer(Hero):
    def __init__(self) -> None:
        super().__init__("archer", 80, 10)


class Mage(Hero):
    def __init__(self) -> None:
        super().__init__("mage", 60, 20)


class Monster(Character):
    def __init__(self, monster_type: str, health: int, attack: int) -> None:
        super().__init__(health, attack)
        self.monster_type = monster_type


class MeleeMonster(Monster):
    def __init__(self) -> None:
        super().__init__("melee", 30, 10)


class ArcherMonster(Monster):
    def __init__(self) -> None:
        super().__init__("archer", 20, 8)


class MagicMonster(Monster):
    def __init__(self) -> None:
        super().__init__("magic", 25, 12)

