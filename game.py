import random

from objects.hero_class import HeroFactory
from objects.item_class import spawn_item


def game() -> None:
    hero_factory = HeroFactory()
    hero_classes = {1: "warrior", 2: "archer", 3: "mage"}
    print("Choose your hero class (warrior, archer, mage): ")
    for key in hero_classes.keys():
        print(key, ". ", hero_classes[key])

    while True:
        try:
            hero_class = hero_classes[int(input())]
            hero = hero_factory.create_hero(hero_class)
            break
        except (KeyError, ValueError):
            print("Invalid input. Please try again.")

    monsters_defeated = 0

    while monsters_defeated < 10:
        monster = hero_factory.create_monster()
        print(f"\nA wild {monster.monster_type} monster appears!")

        while not hero.is_dead() and not monster.is_dead():
            available_attacks = {1: "sword"}
            if hero.inventory["bow"] and hero.inventory["arrows"] > 0:
                available_attacks[2] = "bow"
            if hero.inventory["spellbook"]:
                available_attacks[3] = "magic"

            print("Choose your attack type:")
            for key, value in available_attacks.items():
                print(key, ". ", value)

            while True:
                try:
                    attack_type = available_attacks[int(input())]
                    break
                except (KeyError, ValueError):
                    print("Invalid input. Please try again.")

            damage = random.randint(hero.attack // 2, hero.attack)
            print(f"\n{hero.hero_class.capitalize()} deals {damage} damage to the {monster.monster_type} monster.")
            monster.take_damage(damage)

            if monster.is_dead():
                print(f"{monster.monster_type.capitalize()} monster is defeated!")
                monsters_defeated += 1

                item = spawn_item()
                print(f"\nYou found a new weapon: {item.item_type}!")
                if item.item_type == "bow" or item.item_type == "sword" or item.item_type == "spellbook":
                    print(f"\nDamage per attack: {item.value}!")
                    hero.pick_item(item.item_type)
                    hero.attack += item.value
                elif item.item_type == "arrows":
                    print(f"\nYou found a {item.item_type}!")
                    hero.inventory["arrows"] += item.value
                elif item.item_type == "apple":
                    print(f"\nYour health was fully restored!")
                    hero.health = 100
                elif item.item_type == "totem":
                    print(f"\nYour game was saved!!")
                    hero.pick_item("totem")

            else:
                damage = random.randint(monster.attack // 2, monster.attack)
                print(f"{monster.monster_type.capitalize()} monster deals {damage} damage to the {hero.hero_class}.")
                hero.take_damage(damage)

            if hero.is_dead():
                if hero.inventory["totem"]:
                    print("\nYou have a totem! Reviving...")
                    hero.health = 100
                    hero.inventory["totem"] = False
                else:
                    print("\nGame Over.")
                    break

            if monsters_defeated == 10:
                print("\nCongratulations! You saved the kingdom!")
