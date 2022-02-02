from dataclasses import dataclass

from game import Game


@dataclass
class Action:
    type: int
    params: list[any]


actions = dict[int, callable]()


def action(_type):
    def decorator(func):
        actions[_type] = lambda game, params: func(game, params)

        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator


@action(0)
def goto(game: Game, params: list[any]):
    game.current_sequence = params[0]


@action(2)
def add_item(game: Game, params: list[any]):
    game.player.items.add()


@action(3)
def consume_item(game: Game, params: list[any]):
    for i,item in enumerate(game.player.items):
        if item.id == params[0]:
            del game.player.items[i]
