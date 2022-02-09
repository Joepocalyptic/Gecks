from dataclasses import dataclass

from objects.achievements import Achievement
from objects.items import Item


@dataclass
class Player:
    name: str
    cash: int
    items: list[Item]


@dataclass
class Save:
    player: Player
    game_flags: list[int]
    current_situation: int
    current_sequence: int

    achievements: list[int]
