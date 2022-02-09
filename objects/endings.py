from dataclasses import dataclass
from json import load as load_json

from objects.situations import Sequence


@dataclass
class Ending:
    id: int
    name: str
    description: str
    achievement: int


def __parse_endings():
    with open("data/endings.json", "r", encoding="utf-8") as file:
        json = load_json(file)

    return [
        Ending(ending["id"], ending["name"], ending["description"], ending["achievement"])
        for ending in json
    ]


parsed_endings = __parse_endings()
