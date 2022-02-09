import pickle

from objects.achievements import parsed_achievements
from objects.actions import parsed_actions
from objects.endings import parsed_endings
from objects.situations import parsed_situations, Sequence
from objects.saves import *


class Game:
    __lock = object()

    def __init__(self, lock, save_data: Save):
        self.stop = False
        self.auto_continue = False

        assert (lock == Game.__lock), \
            "Game may not be instantiated directly; use Game#from_file(filename) or Game#new()"

        self.player = save_data.player
        self.game_flags = save_data.game_flags
        self.current_situation = save_data.current_situation
        self.current_sequence = save_data.current_sequence
        self.achievements = save_data.achievements

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
            game_flags=list[int](),
            current_sequence=0,
            current_situation=0,
            achievements=list[Achievement]()
        ))

    def play(self):
        self.run_situation(parsed_situations[self.current_situation])

    def run_situation(self, situation):
        for i in range(self.current_sequence, len(situation.sequences)):
            if self.stop: return
            self.run_sequence(situation.sequences[i])

        self.run_situation(parsed_situations[self.current_situation])

    def run_sequence(self, sequence: Sequence):
        print()
        if not sequence.text == "":
            print(f"{sequence.actor + ': ' if sequence.actor != '' else ''}{format_dialogue(sequence.text, self)}")

        for action in sequence.actions:
            self.run_action(action)

        if self.stop: return

        if len(sequence.branches) > 0:
            self.run_sequence(get_branch(sequence.branches))
        elif not self.auto_continue:
            input("\nPress enter to continue... ")

        self.auto_continue = False

    def run_action(self, action: dict):
        parsed_actions[action["id"]](self, action["params"])

    def trigger_ending(self, id_: int):
        self.stop = True
        ending = next((ending for ending in parsed_endings if ending.id == id_), None)

        print(f"\nTHE END: {ending.name}")
        print(f"\n{format_dialogue(ending.description, self)}")
        self.add_achievement(ending.achievement)

    def add_achievement(self, id_: int):
        self.achievements.append(id_)
        achievement = next((achievement for achievement in parsed_achievements if achievement.id == id_), None)

        print(f"\nYou obtained an achievement: \"{achievement.name}\"!")


def format_dialogue(text, game: Game):
    words = text.split()
    new_text = ""
    word_count = 0
    for word in words:
        word = word.format(name=game.player.name)
        new_text += word + " "
        word_count += 1
        if word_count == 20:
            new_text += "\n"
            word_count = 0

    return new_text


def get_branch(branches):
    print()
    for i, branch in enumerate(branches):
        print(f"{i + 1}.) {branch.choice}")

    while True:
        try:
            choice = int(input("\nPlease enter your choice: "))
            return branches[choice - 1]
        except (ValueError, IndexError):
            print("Invalid input.")
            continue
