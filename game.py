import pickle

from objects.saves import *
from objects.situations import *


class Game:
    exit = False

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
            current_sequence=0,
            current_situation=0,
            achievements=list()
        ))

    def play(self):
        self.__run_situation()

    def __run_situation(self):
        pass
        # situation = parsed_situations[self.current_situation]

        # for i in range(self.current_sequence, len(parsed_situations)):
        #    if not self.__run_sequence(situation[i]):
        #        break

        #self.__run_situation()


    def __run_sequence(self, branch=False):
        situation = parsed_situations[self.current_situation]

        if len(situation.branches) > 0:
            for branch in situation.branches:
                branch

        input("\nPress enter to continue...")
        return True