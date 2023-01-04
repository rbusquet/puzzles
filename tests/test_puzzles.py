import pytest

from puzzles_py import __version__
from puzzles_py.capital_after_vowel import (
    capital_after_vowel,
    capital_after_vowel_regexp,
    capital_after_vowel_regexp_v2,
)
from puzzles_py.rotate_tetromino import rotate_tetromino


def test_version():
    assert __version__ == "0.1.0"


@pytest.mark.skip("not implemented")
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
    assert "heLlo WoRld" == capital_after_vowel_regexp_v2("hello world")
    assert "xaaBeueKaDii" == capital_after_vowel_regexp_v2("xaabeuekadii")
