from dataclasses import dataclass
from json import load as load_json

from objects.actions import Action


@dataclass
class BranchSequence:
    id: int
    actor: str
    text: str
    actions: list[Action]
    branches: list


@dataclass
class Sequence:
    id: int
    actor: str
    text: str
    actions: list[Action]
    branches: list[BranchSequence]


@dataclass
class Situation:
    id: int
    sequences: list


def __parse_situations():
    with open("../data/situations.json", "r", encoding="utf-8") as file:
        json = load_json(file)

    return [Situation(situation.id, [
                Sequence(sequence["id"], sequence["actor"], sequence["text"], sequence["actions"], sequence["branches"])
                for sequence in situation.sequences])
            for situation in json]


parsed_situations = __parse_situations()
import pprint
pprint.pprint(parsed_situations)
