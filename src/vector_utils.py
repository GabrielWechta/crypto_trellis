from typing import List


def dot_prod(vec1: List[int | float], vec2: List[int | float]) -> int | float:
    return sum([el1 * el2 for el1, el2 in zip(vec1, vec2)])


def scalar_prod(scalar: int | float, vec: List[int | float]) -> List[int | float]:
    return [el * scalar for el in vec]


def add_vectors(vec1: List[int | float], vec2: List[int | float]) -> List[int | float]:
    return [el1 + el2 for el1, el2 in zip(vec1, vec2)]


def sub_vectors(vec1: List[int | float], vec2: List[int | float]) -> List[int | float]:
    return [el1 - el2 for el1, el2 in zip(vec1, vec2)]
