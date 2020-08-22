import random
from typing import Iterable, Union


def Choice(choices: Iterable, weights: Iterable[Union[int,float]] = None, *,
           cum_weights: Iterable[Union[int,float]] = None):
    """Generates numbers from a list.

    :param choices: Choices to generate.
    :return:
    """
    # Range check.
    choices = list(choices).copy()
    assert len(choices) > 0

    if weights or cum_weights:
        def rand():
            return random.choices(choices, weights, cum_weights=cum_weights)
    else:
        def rand():
            return random.choice(choices)

    return rand
