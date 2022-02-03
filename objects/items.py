from dataclasses import dataclass


@dataclass
class Item:
    id: int
    name: str


parsed_items = list[Item]()
