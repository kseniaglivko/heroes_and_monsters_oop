statistics_schema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://example.com/product.schema.json",
    "type": "object",
    "title": "Статистика игры.",
    "description": "В схеме содержится информация о состоянии игрового процесса.",
    "properties": {
        "monster_counter": {"value": "int"},
        "hero": {
            "type": {"type": "string", "enum": ["Маг", "Мечник", "Лучник"]},
            "power": {"type": "int"},
            "hp": {"type": "int"},
        },
        "monster": {
            "type": {
                "type": "string",
                "enum": ["Злой колдун", "Скелет-лучник", "Гоблин-мечник"],
            },
            "power": {"type": "int"},
            "hp": {"type": "int"},
        },
        "inventory": {"type": "array"},
    },
}
