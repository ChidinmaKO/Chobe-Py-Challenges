IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    new_names = []
    for name in names:
        name = name.lower()
        if name.startswith(IGNORE_CHAR):
            continue
        if not (name.isalpha()):
            continue
        if name.startswith(QUIT_CHAR):
            break
        new_names.append(name)
        if len(new_names) == MAX_NAMES:
            break
    return new_names


# tests
import pytest

from control_flow import filter_names


@pytest.mark.parametrize("names, expected_return", [
    (['bob'], []),
    (['bob', 'berta'], []),
    (['quit', 'ana'], []),
    (['12', 'bas'], []),
    (['ana', 'bob'], ['ana']),
    (['ana', 'bob', 'quinton'], ['ana']),
    (['bob', 'ana', 'quinton'], ['ana']),
    (['tim', 'ana', 'quinton'], ['tim', 'ana']),
    (['tim', 'quinton', 'ana'], ['tim']),
    (['tim', '1quinton', 'ana'], ['tim', 'ana']),
    (['t2im', '1quinton', 'ana'], ['ana']),
    (['t2im', '1quinton', 'a3na', '4'], []),
    (['tim', 'amber', 'ana', 'cindy', 'sara', 'molly', 'henry'],
     ['tim', 'amber', 'ana', 'cindy', 'sara']),
    (['tim', 'amber', 'ana', 'c1ndy', 'sara', 'molly', 'henry'],
     ['tim', 'amber', 'ana', 'sara', 'molly']),
])
def test_filter_names(names, expected_return):
    assert list(filter_names(names)) == expected_return