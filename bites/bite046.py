def fizzbuzz(num):
#     if num % 15 == 0:
#         return f"Fizz Buzz"
#     elif num % 5 == 0:
#         return f"Buzz"
#     elif num % 3 == 0:
#         return f"Fizz"
#     return num

#  using recursion
    if num == 0:
        return
    fizzbuzz(num - 1)
    if num % 15 == 0:
        return f"Fizz Buzz"
    elif num % 5 == 0:
        return f"Buzz"
    elif num % 3 == 0:
        return f"Fizz"
    return num



# tests
import pytest

# from fizzbuzz import fizzbuzz

@pytest.mark.parametrize("arg, ret",[
    (1, 1),
    (2, 2),
    (3, 'Fizz'),
    (4, 4),
    (5, 'Buzz'),
    (6, 'Fizz'),
    (7, 7),
    (8, 8),
    (9, 'Fizz'),
    (10, 'Buzz'),
    (11, 11),
    (12, 'Fizz'),
    (13, 13),
    (14, 14),
    (15, 'Fizz Buzz'),
    (16, 16),
])
def test_fizzbuzz(arg, ret):
    assert fizzbuzz(arg) == ret