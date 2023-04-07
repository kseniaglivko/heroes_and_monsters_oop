import random


class Item:
    def __init__(self, item_type: str, value: int):
        self.item_type = item_type
        self.value = value


def spawn_item() -> Item:
    item_types = ["bow", "sword", "spellbook", "arrows", "apple", "totem"]
    item_type = random.choice(item_types)
    value = random.randint(1, 20)
    return Item(item_type, value)
