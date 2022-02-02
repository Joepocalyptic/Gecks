from dataclasses import dataclass
import json

from objects.achievements import Achievement
from objects.items import Item


@dataclass
class Player:
    name: str
    money: int
    items: list[Item]


@dataclass
class Save:
    player: Player
    time: str
    game_flags: list[int]
    current_situation: int
    current_sequence: int

    achievements: list[Achievement]
