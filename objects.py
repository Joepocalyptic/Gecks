from dataclasses import dataclass
from json import load as load_json


@dataclass
class Action:
    type: int
    params: list[int]


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
    branches: list[BranchSequence
    ]


@dataclass
class Situation:
    id: int
    sequences: list


def __parse_scenes():
    with open("data/scenes.json", "r", encoding="utf-8") as file:
        json = load_json(file)

    for situation in json:
        sit = Situation(**situation)

        sequences = []
        for sequence in sit.sequences:
            sequences.append(Sequence(sequence["id"], sequence["actor"], sequence["text"], sequence["actions"], sequence["branches"]))

            for seq in sequences:
                print(seq)

    return json


scenes = __parse_scenes()