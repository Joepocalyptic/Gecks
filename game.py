import pickle

from objects.saves import *


class Game:
    __lock = object()

    def __init__(self, lock, save_data: Save):
        assert(lock == Game.__lock), \
                "Game may not be instantiated directly; use Game#from_file(filename) or Game#new()"

        self.current_situation = save_data.current_situation
        self.current_sequence = save_data.current_sequence
        self.player = save_data.player

    @classmethod
    def from_file(cls, filename: str):
        with open(filename, "rb") as f:
            save_data: Save = pickle.load(f)
            return Game(cls.__lock, save_data)

    @classmethod
    def new(cls):
        return Game(cls.__lock, Save(
            player=Player(
                "",
                0,
                list()
            ),
            time="",
            game_flags=list(),
            current_location=0,
            achievements=list()
        ))
