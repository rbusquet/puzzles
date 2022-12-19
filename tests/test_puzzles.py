from puzzles import __version__
from puzzles.capital_after_vowel import capital_after_vowel, capital_after_vowel_regexp
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


def test_capital_after_vowel():
    assert "heLlo WoRld" == capital_after_vowel("hello world")
    assert "xaaBeueKaDii" == capital_after_vowel("xaabeuekadii")
    assert "heLlo WoRld" == capital_after_vowel_regexp("hello world")
    assert "xaaBeueKaDii" == capital_after_vowel_regexp("xaabeuekadii")
