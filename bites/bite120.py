from functools import wraps


def int_args(func):
    @wraps(func)
    # complete this decorator
    def inner(*args):
        is_ints = [isinstance (i, int) for i in args]
        if not all(is_ints):
            raise TypeError("Not an integer")
            
        is_greater_than_zero = [i > 0 for i in args]
        if not all(is_greater_than_zero):
            raise ValueError("Less than 0")
        return func(*args)
    return inner

# tests
import pytest

from validate import int_args


@int_args
def sum_numbers(*numbers):
    return sum(numbers)


def test_valid_args():
    assert sum_numbers(1, 2, 3) == 6


def test_invalid_type_str():
    with pytest.raises(TypeError):
        sum_numbers(1, 'string', 3)


def test_invalid_type_float():
    with pytest.raises(TypeError):
        sum_numbers(1, 2.1, 3)


def test_negative_number():
    with pytest.raises(ValueError):
        sum_numbers(1, 2, -3)