from typing import Callable


def IdGenerator() -> Callable[[], int]:

    id = 0
    def id_generator():
        nonlocal id
        id += 1
        return id
    return id_generator
