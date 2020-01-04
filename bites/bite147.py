from datetime import date

from dateutil.rrule import rrule, DAILY

TODAY = date(year=2018, month=11, day=29)


def get_hundred_weekdays(start_date=TODAY):
    """Return a list of hundred date objects starting from
       start_date up till 100 weekdays later, so +100 days
       skipping Saturdays and Sundays"""
    getdays = list(rrule(DAILY, count=100, dtstart=start_date, byweekday=range(5)))
    result = list(day.date() for day in getdays)
    return result

# tests
from datetime import date, timedelta

from hundred_days import get_hundred_weekdays, TODAY

OTHER_START_DATE = TODAY + timedelta(days=55)


def test_get_hundred_weekdays_default_start_date():
    days = get_hundred_weekdays(start_date=TODAY)
    assert len(days) == 100
    # check start and end dates
    assert days[0] == TODAY
    assert days[-1] == date(2019, 4, 17)
    # check if weekends are not included
    assert days[1] == date(2018, 11, 30)
    assert days[2] == date(2018, 12, 3)
    fri_index = days.index(date(2019, 1, 18))
    assert days[fri_index + 1] == date(2019, 1, 21)


def test_get_hundred_weekdays_different_start_date():
    days = get_hundred_weekdays(start_date=OTHER_START_DATE)
    assert len(days) == 100
    # check start and end dates
    assert days[0] == OTHER_START_DATE
    assert days[-1] == date(2019, 6, 11)
    # check if weekends are not included
    assert days[2] == date(2019, 1, 25)
    assert days[3] == date(2019, 1, 28)
    fri_index = days.index(date(2019, 6, 7))
    assert days[fri_index + 1] == date(2019, 6, 10)