import itertools
import string

# letters = string.ascii_uppercase
# count = list(range(1,27))

# def sequence_generator():
#     result = itertools.cycle((num for letter in zip(count, letters) for num in letter))
#     return result



def sequence_generator():
    alpha = string.ascii_uppercase
    letters = itertools.cycle(alpha)
    count = itertools.cycle(range(1, len(alpha)+1))

    for num, letter in zip(count, letters):
        yield num
        yield letter
    

from itertools import islice

import pytest

from sequence_generator import sequence_generator


@pytest.fixture
def gen():
    """Return a fresh new generator object for each test"""
    return sequence_generator()


def test_first_ten_first_round(gen):
    expected = [1, 'A', 2, 'B', 3, 'C', 4, 'D', 5, 'E']
    # generators == use islice, a regular slicing on a list object == hang
    # because it tries to load in an infinite iterator = not good.
    # don't believe me? change the line below to: `actual = list(gen)[:10]`
    actual = list(islice(gen, 10))
    assert expected == actual


def test_first_ten_second_round(gen):
    expected = [1, 'A', 2, 'B', 3, 'C', 4, 'D', 5, 'E']
    actual = list(islice(gen, 52, 62))  # zero-based
    assert expected == actual


def test_last_ten_third_round(gen):
    expected = [22, 'V', 23, 'W', 24, 'X', 25, 'Y', 26, 'Z']
    actual = list(islice(gen, 146, 156))
    assert expected == actual