import random
from typing import Iterable

import scipy.stats


def RandomChoice(choices: Iterable):
    """Generates numbers from a list.

    :param choices: Choices to generate.
    :return:
    """
    # Range check.
    choices = list(choices).copy()
    assert len(choices) > 0

    def gen():
        while True:
            yield random.choice(choices)

    return gen()
