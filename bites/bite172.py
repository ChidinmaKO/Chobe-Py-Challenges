from functools import partial

# create 2 partials:
# - 'rounder_int' rounds to int (0 places)
# - 'rounder_detailed' rounds to 4 places

rounder_int =  partial(round, ndigits = 0)
rounder_detailed =  partial(round, ndigits = 4)

# tests
# from curry import rounder_int, rounder_detailed


def test_rounder_int_partial():
    assert rounder_int(1.3434587383) == 1
    assert rounder_int(10.42342) == 10
    assert rounder_int(1.99) == 2


def test_rounder_detailed_partial():
    assert rounder_detailed(1.344587383) == 1.3446
    assert rounder_detailed(10.42342) == 10.4234
    assert rounder_detailed(1.99) == 1.9900