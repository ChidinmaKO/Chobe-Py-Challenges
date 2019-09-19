from typing import List

def sum_numbers(numbers: List[int])-> int:
    """Sums numbers

    :param numbers: a list of numbers
    :type numbers: list
    :raises TypeError: if not all numeric values passed in
    :return: sum of numbers
    :rtype: int
    """
    pass

# tests

# import typing

# from annotations import sum_numbers


def test_sum_numbers():
    res = sum_numbers.__annotations__
    assert res.get('numbers') == typing.List[int]
    assert res.get('return') == int