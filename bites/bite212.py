from contextlib import suppress


def sum_numbers(numbers):
    """This generator divides each nummber by its consecutive number.
       So if it gets passed in [4, 2, 1] it yields 4/2 and 2/1.
       It ignores ZeroDivisionError and TypeError exceptions (latter happens
       when a string or other non-numeric data type is in numbers)

       Task: use contextlib's suppress twice to make the code below more concise.
    """
    for i, j in zip(numbers, numbers[1:]):
        with suppress(ZeroDivisionError, TypeError):
            yield i/j


# tests
import inspect

from summing import sum_numbers


def test_functionality():
    numbers = [1, 2, 0, 4, 5, 12, 'a', 3]
    actual = list(sum_numbers(numbers))
    expected = [0.5, 0.0, 0.8, 0.4166666666666667]
    assert actual == expected


def test_use_of_idioms():
    src = inspect.getsource(sum_numbers)
    assert 'try' not in src
    assert 'except ' not in src
    assert 'yield' in src
    assert 'TypeError' in src
    assert 'ZeroDivisionError' in src
    assert src.count('suppress(') in (1, 2)
    assert src.count('with') in (1, 2)