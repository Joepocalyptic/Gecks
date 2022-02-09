from dataclasses import dataclass
from json import load as load_json


@dataclass
class Achievement:
    id: int
    name: str


def __parse_achievements():
    with open("data/achievements.json", "r", encoding="utf-8") as file:
        json = load_json(file)

    return [
        Achievement(achievement["id"], achievement["name"])
        for achievement in json
    ]


parsed_achievements = __parse_achievements()
