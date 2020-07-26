def IdGen() -> int:
    i = 0
    while True:
        i = i + 1
        yield i
