import atexit
from game import Game

# noinspection PyTypeChecker
from util import save_handler

game: Game = None


def main():
    global game
    game = Game(save_handler.load_game())
    game.play()

    atexit.register(exit_handler)


if __name__ == "__main__":
    main()


def exit_handler():
    global game
    save_handler.save_game(game)