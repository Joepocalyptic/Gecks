from dataclasses import dataclass

from objects.items import parsed_items


@dataclass
class Action:
    type: int
    params: list[any]


parsed_actions = dict[int, callable]()


def action(_type):
    def decorator(func):
        parsed_actions[_type] = lambda game, params: func(game, params)

        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator


@action(0)
def goto(game, params: list[any]):
    game.current_sequence = params[0]
    print("test")


@action(2)
def add_item(game, params: list[any]):
    game.player.items.append(parsed_items[params])


@action(3)
def consume_item(game, params: list[any]):
    for i,item in enumerate(game.player.items):
        if item.id == params[0]:
            del game.player.items[i]


@action(4)
def reduce_cash(game, params: list[any]):
    game.player.cash = game.player.cash - (game.player.cash * (params[0] / 100))


@action(95)
def random_branch(game, params: list[any]):
    game = game.player.cash - (game.player.cash * (params[0] / 100))


@action(99)
def trigger_ending(game, params: list[any]):
    pass