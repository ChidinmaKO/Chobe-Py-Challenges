from functools import wraps

MAX_RETRIES = 3


class MaxRetriesException(Exception):
    pass


def retry(func):
    """Complete this decorator, make sure
       you print the exception thrown"""
    # ... retry MAX_RETRIES times
    # ...
    # make sure you include this for testing:
    # except Exception as exc:
    #     print(exc)
    # ...
    # and use wraps to preserve docstring
    #
    @wraps(func)
    def wrapper(*args, **kwargs):
        for tries in range(1, MAX_RETRIES + 1):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(e)
        else:
            raise MaxRetriesException("Max Retries Exceeded")
    return wrapper

# tests
import random
import re

import pytest

from decorators import (retry,
                        MaxRetriesException,
                        MAX_RETRIES)


@retry
def get_two_numbers(numbers):
    """Give a list of items pick 2 random ones,
       if both are not ints raise a ValueError
    """
    chosen = random.sample(numbers, 2)
    if not all(type(i) == int for i in chosen):
        raise ValueError('not all ints')


def test_bad_data_max_retries_and_exception(capfd):
    with pytest.raises(MaxRetriesException):
        get_two_numbers(['a', 'b'])
    output = capfd.readouterr()[0]
    assert output.count('not all ints') == MAX_RETRIES


def test_good_data_no_retry_and_no_exception(capfd):
    get_two_numbers([1, 2, 3])
    output = capfd.readouterr()[0]
    assert output.count('not all ints') == 0


def test_decorated_function_preserves_docstring(capfd):
    docstring = get_two_numbers.__doc__
    assert docstring is not None
    line1 = "Give a list of items pick 2 random ones,"
    line2 = "if both are not ints raise a ValueError"
    assert re.search(rf'{line1}\s+{line2}', docstring)