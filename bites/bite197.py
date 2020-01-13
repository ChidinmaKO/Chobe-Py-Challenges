from datetime import date
from dateutil.relativedelta import relativedelta, SU


def get_mothers_day_date(year: int) -> date:
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    # one way - from the beginning of the year
    # mothers_sunday = date(year, 1, 1) + relativedelta(months=4, weekday=SU(2))
    
    # another way -  from the first day in May
    mothers_sunday = date(year, month=5, day=1) + relativedelta(weekday=SU(2))
    return mothers_sunday


# tests
from datetime import date

import pytest

from mday import get_mothers_day_date


def test_check_type():
    assert type(get_mothers_day_date(2019)) == date


@pytest.mark.parametrize('arg,expected', [
    (2014, date(2014, 5, 11)),
    (2015, date(2015, 5, 10)),
    (2016, date(2016, 5, 8)),
    (2017, date(2017, 5, 14)),
    (2018, date(2018, 5, 13)),
    (2019, date(2019, 5, 12)),
    (2020, date(2020, 5, 10)),
    (2021, date(2021, 5, 9)),
    (2022, date(2022, 5, 8)),
    (2023, date(2023, 5, 14)),
    (2024, date(2024, 5, 12)),
])
def test_return_various_years(arg, expected):
    assert get_mothers_day_date(arg) == expected