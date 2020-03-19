import types
from itertools import islice


def group(iterable, n):
    """Splits an iterable set into groups of size n and a group
       of the remaining elements if needed.

       Args:
         iterable (list): The list whose elements are to be split into
                          groups of size n.
         n (int): The number of elements per group.

       Returns:
         list: The list of groups of size n,
               where each group is a list of n elements.
    """
    result = []
    iterable = list(iterable)
    
    for i in range(0, len(iterable), n):
        result.append(iterable[i: i+n])
    return result
    
    # another way
    # iterator = iter(iterable)
    # result = list(iter(lambda: list(islice(iterator, n)), []))
    # return result
    


if __name__ == '__main__':
    iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 3
    ret = group(iterable, n)
    print(ret)


# TESTS
import types

from grouping import group


def test_split_10_ints_by_3():
    iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 3
    actual = group(iterable, n)
    expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
    assert actual == expected


def test_passing_in_tuple():
    iterable = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    n = 3
    actual = group(iterable, n)
    expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
    assert actual == expected


def test_passing_in_generator():
    iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    gen = (i for i in iterable)
    assert isinstance(gen, types.GeneratorType)
    n = 3
    actual = group(gen, n)
    expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert actual == expected


def test_different_iterable_size():
    iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 2
    n = 3
    actual = group(iterable, n)
    expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 1, 2],
                [3, 4, 5], [6, 7, 8], [9, 10]]
    assert actual == expected


def test_different_n():
    iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 2
    n = 5
    actual = group(iterable, n)
    expected = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],
                [1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
    assert actual == expected