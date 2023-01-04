import re
import string
from typing import Iterator


def capital_after_vowel(text: str) -> str:
    """
    >>> capital_after_vowel("hello world")
    'heLlo WoRld'
    >>> capital_after_vowel("xaabeuekadii")
    'xaaBeueKaDii'
    """

    def iterator(word: str) -> Iterator[str]:
        capitalize = False
        for letter in word:
            if letter in "aeiou":
                capitalize = True
            elif capitalize and letter in string.ascii_letters:
                yield letter.capitalize()
                capitalize = False
                continue
            yield letter

    return "".join(iterator(text))


def capital_after_vowel_regexp(text: str) -> str:
    """
    >>> capital_after_vowel_regexp("hello world")
    'heLlo WoRld'
    >>> capital_after_vowel_regexp("xaabeuekadii")
    'xaaBeueKaDii'
    """

    def replace(m: re.Match) -> str:
        return f"{m[1]}{m[2].upper()}"

    after_vowels = re.compile(
        r"""
        (
            [aeiou]  # match a vowel + 0-n spaces/non-letters
        )  # group 1
        (
            \s*  # any spaces
            (?![aeiou])  # negative lookahead--exclude vowels
            [a-z]  # match a-z minus vowels
        )  # group 2
        """,
        re.VERBOSE,
    )

    return after_vowels.sub(replace, text)


def capital_after_vowel_regexp_v2(text: str) -> str:
    """
    >>> capital_after_vowel_regexp_v2("hello world")
    'heLlo WoRld'
    >>> capital_after_vowel_regexp_v2("xaabeuekadii")
    'xaaBeueKaDii'
    """

    def replace(m: re.Match) -> str:
        return m[1].upper()

    after_vowels = re.compile(
        r"""
        (?<=[aeiou])  # positive lookbehind: assert matches a vowel before group
        (
            \s*  # any whitespace character
            (?![aeiou])  # negative lookahead--exclude vowels
            [a-z]  # letters from a to z
        )  # group 1
        """,
        re.VERBOSE,
    )

    return after_vowels.sub(replace, text)
