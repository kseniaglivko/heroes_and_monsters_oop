statistics_schema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://example.com/product.schema.json",
    "type": "object",
    "title": "Статистика игры.",
    "description": "В схеме содержится информация о состоянии игрового процесса.",
    "properties": {
        "monster_counter": "int",
        "totem": "int",
        "arrows": {
            "quantity": "int",
            "power": "int"
        },
        "bow": {"quantity": "int"},
        "sword": {
            "quantity": "int",
            "power": "int"
        },
        "spell": {
            "type": [
                "заклинание школы магии огня 'Огненный шар'",
                "заклинание школы магии воды 'Ледяная стрела'",
                "заклинание школы магии земли 'Землетрясение'",
                "заклинание школы магии воздуха 'Молния'",
                "заклинание школы магии огня 'Огненный элементаль'",
                "заклинание школы магии воды 'Водный элементаль'",
                "заклинание школы магии земли 'Земляной элементаль'",
                "заклинание школы магии воздуха 'Воздушный элементаль'",
            ],
            "quantity": "int",
            "power": "int"
        },
        "hero": {
            "type": ["Маг", "Мечник", "Лучник"],
            "power": {"type": "int"},
            "hp": {"type": "int"},
        },
        "monster": {
            "power": {"type": "int"},
            "hp": {"type": "int"},
        },
    },
}
