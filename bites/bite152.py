from functools import wraps


DEFAULT_TEXT = ('Subscribe to our blog (sidebar) to periodically get '
                'new PyBites Code Challenges (PCCs) in your inbox')
DOT = '.'


def strip_range(start, end):
    """Decorator that replaces characters of a text by dots, from 'start'
       (inclusive) to 'end' (exclusive) = like range.

        So applying this decorator on a function like this and 'text'
        being 'Hello world' it would convert it into 'Hel.. world' when
        applied like this:

        @strip_range(3, 5)
        def gen_output(text):
            return text
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = ""
            for index, char in enumerate(func(*args, **kwargs)):
                if start <= index < end:
                    result += DOT
                else:
                    result += char
            return result
        return wrapper
    return decorator
            
# tests

import pytest

# from decorator import strip_range

TEXTS = ['Hello world', 'Welcome to PyBites',
         'Decorators for fun and profit']


@pytest.mark.parametrize("start, end, arg, expected", [
    (3, 5, TEXTS[0], 'Hel.. world'),
    (4, 8, TEXTS[0], 'Hell....rld'),
    (0, 3, TEXTS[1], '...come to PyBites'),
    (-1, 3, TEXTS[1], '...come to PyBites'),
    (0, -1, TEXTS[1], 'Welcome to PyBites'),
    (5, 10, TEXTS[2], 'Decor..... for fun and profit'),
    (100, 110, TEXTS[2], 'Decorators for fun and profit'),
    (20, 100, TEXTS[2], 'Decorators for fun a.........'),
])
def test_strip_range(start, end, arg, expected):
    @strip_range(start, end)
    def gen_output(text):
        return text
    actual = gen_output(text=arg)
    assert actual == expected