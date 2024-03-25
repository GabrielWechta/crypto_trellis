from typing import List


def dot_prod(vec1: List[int | float], vec2: List[int | float]) -> int | float:
    return sum([el1 * el2 for el1, el2 in zip(vec1, vec2)])
