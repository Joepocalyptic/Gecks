from dataclasses import dataclass
from json import load as load_json

from objects.actions import Action


@dataclass
class BranchSequence:
    choice: int
    actor: str
    text: str
    actions: list[Action]
    branches: list


@dataclass
class Sequence:
    id: int
    actor: str
    text: str
    actions: list[dict]
    branches: list[BranchSequence]


@dataclass
class Situation:
    id: int
    sequences: list


def __parse_situations():
    with open("data/situations.json", "r", encoding="utf-8") as file:
        json = load_json(file)

    def parse_branches(branches):
        _branches = list[BranchSequence]()

        for branch in branches:
            if len(branch["branches"]) > 0:
                branch["branches"] = parse_branches(branch["branches"])

            _branches.append(BranchSequence(
                choice=branch["choice"],
                actor=branch["actor"],
                text=branch["text"],
                actions=branch["actions"],
                branches=branch["branches"]
            ))

        return _branches

    return [
        Situation(situation["id"], [
            Sequence(sequence["id"], sequence["actor"], sequence["text"], sequence["actions"], parse_branches(sequence["branches"]))
            for sequence in situation["sequences"]
            ])
        for situation in json
    ]


parsed_situations = __parse_situations()
