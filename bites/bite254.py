num_hundreds = -1


def sum_numbers(numbers: list) -> int:
    """Sums passed in numbers returning the total, also
       update the global variable num_hundreds with the amount
       of times 100 fits in total"""
    global num_hundreds
    total = sum(numbers, 0)
    num_hundreds += total // 100
    return total

# tests
import pytest

from scoping import sum_numbers


@pytest.mark.parametrize("arg, ret, hundreds_value", [
    ([], 0, -1),
    ([1, 2, 3], 6, -1),
    ([40, 50, 60], 150, 0),
    ([140, 50, 60], 250, 2),
    ([140, 150, 160], 450, 6),
    ([1140, 150, 160], 1450, 20),
])
def test_sum_numbers(arg, ret, hundreds_value):
    assert sum_numbers(arg) == ret
    from scoping import num_hundreds
    assert num_hundreds == hundreds_value