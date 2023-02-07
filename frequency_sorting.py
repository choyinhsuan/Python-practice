from collections.abc import Iterable


def frequency_sorting(numbers: list[int]) -> Iterable[int]:
    # replace this for solution
    numbers.sort()
    return sorted(numbers,key=lambda x: numbers.count(x), reverse=True)