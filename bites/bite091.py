import typing

VOWELS = 'aeiou'
PYTHON = 'python'


def contains_only_vowels(input_str: str) -> bool:
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    return all(char in VOWELS for char in input_str.lower())


def contains_any_py_chars(input_str: str) -> bool:
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    return any(char in PYTHON for char in input_str.lower())


def contains_digits(input_str: str) -> bool:
    """Receives input string and checks if it contains
       one or more digits."""
    return any(char.isdigit() for char in input_str)

# tests
import pytest

from anyall import (contains_only_vowels,
                    contains_any_py_chars,
                    contains_digits)


@pytest.mark.parametrize("arg, expected", [
    ('aioue', True),
    ('EoUia', True),
    ('aaAiIee', True),
    ('AEIOU', True),
    ('aaeeouu', True),
    ('abcde', False),
    ('AE123', False),
    ('AiOuef', False),
])
def test_contains_only_vowels(arg, expected):
    assert bool(contains_only_vowels(arg)) is expected


@pytest.mark.parametrize("arg, expected", [
    ('Python', True),
    ('pycharm', True),
    ('PYTHON', True),
    ('teaser', True),
    ('bob', True),
    ('julian', True),
    ('yes', True),
    ('no', True),
    ('america', False),
    ('B@b', False),
    ('Jules', False),
    ('agua', False),
    ('123', False),
    ('', False),
])
def test_contains_any_py_chars(arg, expected):
    assert bool(contains_any_py_chars(arg)) is expected


@pytest.mark.parametrize("arg, expected", [
    ('yes1', True),
    ('123', True),
    ('hello2', True),
    ('up2date', True),
    ('yes', False),
    ('hello', False),
    ('', False),
])
def test_contains_digits(arg, expected):
    assert bool(contains_digits(arg)) is expected