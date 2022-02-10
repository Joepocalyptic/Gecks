from game import Game
from os.path import exists
import pickle

from objects.saves import *

save_location = "user/save.bin"


def save_game(save: Save):
    print("\nSaving game...")

    with open("user/save.bin", "wb") as file:
        pickle.dump(save, file)

    print("\nGame saved.")


# noinspection PyBroadException
def load_game() -> Save:
    default_save = Save(
        player=Player(
            "",
            100,
            list()
        ),
        game_flags=list[int](),
        current_sequence=0,
        current_situation=0,
        achievements=list[int]()
    )
    if exists("user/save.bin"):
        with open("user/save.bin", "rb") as file:
            try:
                print("Save file detected! Loading existing game.")
                return pickle.load(file)
            except Exception:
                print("WARNING: Failed to warn save data; the file may be corrupt. Starting a new game.")
                save_game(default_save)
                return default_save

    else:
        print("Save file does not exist! Starting a new game.")
        save_game(default_save)
        return default_save
