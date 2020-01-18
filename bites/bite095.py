MSG = 'Hey {}, there are more people with your birthday!'


class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)

    def __setitem__(self, name, birthday):
        if any(((i.day == birthday.day) and (i.month == birthday.month)) for (_, i) in self.items()):
            print(MSG.format(name))
        super(BirthdayDict, self).__setitem__(name, birthday)
        # another way 
        # for dt in self.values():
        #     if ((dt.day, dt.month) == (birthday.day, birthday.month)):
        #         print(MSG.format(name))
        # super().__setitem__(name, birthday)


# tests
from datetime import date

import pytest

from bdaydict import BirthdayDict, MSG


@pytest.fixture(scope='module')
def bd():
    """This creates a bday dict that can be shared among the tests
       (scope = module)"""
    return BirthdayDict()


def test_2_bdays_different_dates_not_print_msg(bd, capfd):
    bd['bob'] = date(1987, 6, 15)
    bd['tim'] = date(1984, 7, 15)
    output = capfd.readouterr()[0].strip()
    assert not output.strip()


def test_another_bday_same_yymmdd_print_msg(bd, capfd):
    bd['mary'] = date(1987, 6, 15)
    output = capfd.readouterr()[0].strip()
    assert output == MSG.format('mary')  # exactly the same as bob


def test_another_bday_same_yymm_diff_day_not_print_msg(bd, capfd):
    # not a bday match
    bd['sara'] = date(1987, 6, 14)
    output = capfd.readouterr()[0].strip()
    assert not output.strip()


def test_another_bday_same_mmdd_diff_year_print_msg(bd, capfd):
    # if same day and month, but different year = match
    bd['mike'] = date(1981, 7, 15)  # same as tim, except year
    output = capfd.readouterr()[0].strip()
    assert output == MSG.format('mike')