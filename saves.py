from dataclasses import dataclass
import json


@dataclass
class Achievement:
    pass


@dataclass
class Item:
    pass


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
    current_location: int

    achievements: list[Achievement]
