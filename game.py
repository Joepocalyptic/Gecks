import pickle

from objects.saves import *
from objects.situations import *


def format_dialogue(text):
    words = text.split()
    new_text = ""
    word_count = 0
    for word in words:
        new_text += word + " "
        word_count += 1
        if word_count == 20:
            new_text += "\n"
            word_count = 0

    return new_text


def get_branch(branches):
    print()
    for i,branch in enumerate(branches):
        print(f"{i + 1}.) {branch.choice}")

    while True:
        try:
            choice = int(input("\nPlease enter your choice: "))
            return branches[choice-1]
        except (ValueError, IndexError):
            print("Invalid input.")
            continue


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
        situation = parsed_situations[self.current_situation]

        for i in range(self.current_sequence, len(situation.sequences)):
            if not self.__run_sequence(situation.sequences[i]):
                break

        self.__run_situation()

    def __run_sequence(self, sequence):
        print()
        if not sequence.text == "":
            print(f"{sequence.actor + ': ' if sequence.actor != '' else ''}{format_dialogue(sequence.text)}")

        if len(sequence.branches) > 0:
            self.__run_sequence(get_branch(sequence.branches))
        else:
            input("\nPress enter to continue... ")
        return True
