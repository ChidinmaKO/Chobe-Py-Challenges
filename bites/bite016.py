from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    td_birthday = timedelta(days = 365)
    td_100 = timedelta(days = 100)
    
    # birthday = PYBITES_BORN + td_birthday
    # day_100 = PYBITES_BORN + td_100
  
    date1 = PYBITES_BORN
    date2 = PYBITES_BORN
    
    while True:
        if (date1 + td_100) < (date2 + td_birthday):
            date1 += td_100
            yield date1
        else:
            date2 += td_birthday
            yield date2

# tests
from itertools import islice

from gendates import gen_special_pybites_dates


def test_gen_special_pybites_dates():
    gen = gen_special_pybites_dates()
    dates = list(islice(gen, 10))

    expected = [datetime(2017, 3, 29, 0, 0),
                datetime(2017, 7, 7, 0, 0),
                datetime(2017, 10, 15, 0, 0),
                datetime(2017, 12, 19, 0, 0),  # PyBites 1 year old
                datetime(2018, 1, 23, 0, 0),
                datetime(2018, 5, 3, 0, 0),
                datetime(2018, 8, 11, 0, 0),
                datetime(2018, 11, 19, 0, 0),
                datetime(2018, 12, 19, 0, 0),  # PyBites 2 years old
                datetime(2019, 2, 27, 0, 0)]

    assert dates == expected