from collections.abc import Iterable


def except_zero(items: list[int]) -> Iterable[int]:
    # your code here
    without0 = [x for x in items if x != 0]
    print(without0)
    without0.sort()
    index = 0
    for i in without0:
        while(items[index] == 0):
            index += 1
        items[index] = i
        index += 1
    return items