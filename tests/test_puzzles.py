from puzzles import __version__
from puzzles.rotate_tetromino import rotate_tetromino


def test_version():
    assert __version__ == "0.1.0"


def test_rotate_tetromino():
    grid = [
        [0, 1, 0, 0],
        [0, 1, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]

    expected = [
        [0, 0, 1, 1],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
    ]

    actual = rotate_tetromino(grid, "clockwise")
    assert expected == actual
