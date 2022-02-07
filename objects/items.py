from dataclasses import dataclass
from json import load as load_json


@dataclass
class Item:
    id: int
    name: str


def __parse_items():
    with open("data/items.json", "r", encoding="utf-8") as file:
        json = load_json(file)

    return [
        Item(item["id"], item["name"])
        for item in json
    ]


parsed_items = __parse_items()
