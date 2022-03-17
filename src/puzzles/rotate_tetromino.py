from typing import Literal, TypeVar
from math import cos, sin


T = TypeVar("T")


rotation_matrices = {
    "clockwise": [
        [0, -1],
        [1, 0],
    ],
    "counterclockwise": [
        [0, 1],
        [-1, 0],
    ],
}


def clockwise(grid):
    ...


def rotate_tetromino(grid: T, direction: Literal["clockwise", "counterclockwise"]) -> T:
    return grid
