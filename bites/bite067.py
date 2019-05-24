from datetime import date, timedelta

start_100days = date(2017, 3, 30)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)


def get_hundred_days_end_date():
    """Return a string of yyyy-mm-dd"""
    end_100days = start_100days + timedelta(days=100)
    end_to_str = end_100days.strftime("%Y-%m-%d")
    return end_to_str


def get_days_between_pb_start_first_joint_pycon():
    """Return the int number of days"""
    duration = pycon_date - pybites_founded
    return duration.days


# tests
from calc_dts import (get_hundred_days_end_date,
                      get_days_between_pb_start_first_joint_pycon)


def test_get_hundred_days_end_date():
    assert get_hundred_days_end_date() == '2017-07-08'


def test_get_days_till_pycon_meetup():
    assert get_days_between_pb_start_first_joint_pycon() == 505