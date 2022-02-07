from dataclasses import dataclass
from json import load as load_json

from objects.situations import Situation, Sequence


@dataclass
class Ending:
    id: int
    name: str
    achievement: int
    sequences: list[Sequence]


def __parse_endings():
    with open("data/endings.json", "r", encoding="utf-8") as file:
        json = load_json(file)

    return [
        Ending(ending["id"], ending["name"], ending["achievement"], [
            Sequence(sequence["id"], sequence["actor"], sequence["text"], [], [])
            for sequence in ending["sequences"]
        ])
        for ending in json
    ]


parsed_endings = __parse_endings()
