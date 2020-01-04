from datetime import date

from dateutil.relativedelta import relativedelta

START_DATE = date(2018, 11, 1)
MIN_DAYS_TO_COUNT_AS_MONTH = 10
MONTHS_PER_YEAR = 12


def calc_months_passed(year:int, month:int, day:int) -> int:
    """Construct a date object from the passed in arguments.
       If this fails due to bad inputs reraise the exception.
       Also if the new date is < START_DATE raise a ValueError.

       Then calculate how many months have passed since the
       START_DATE constant. We suggest using dateutil.relativedelta!

       One rule: if a new month is >= 10 (MIN_DAYS_TO_COUNT_AS_MONTH)
       days in, it counts as an extra  month.

       For example:
       date(2018, 11, 10) = 9 days in => 0 months
       date(2018, 11, 11) = 10 days in => 1 month
       date(2018, 12, 11) = 1 month + 10 days in => 2 months
       date(2019, 12, 11) = 1 year + 1 month + 10 days in => 14 months
       etc.

       See the tests for more examples.

       Return the number of months passed int.
    """
    try:
        end_date = date(year, month, day)
    except TypeError as t:
        raise TypeError(f"Inappropriate argument type.{t}")
    
    if end_date < START_DATE:
        raise ValueError(f"End date {end_date} can't be before the start date {START_DATE}")
    
    delta = relativedelta(end_date, START_DATE)
    
    total_months_passed = (delta.years * MONTHS_PER_YEAR) + delta.months
    
    if delta.days >= MIN_DAYS_TO_COUNT_AS_MONTH:
        total_months_passed += 1
    
    return total_months_passed

# tests
import pytest

from months import calc_months_passed


def test_same_date():
    assert calc_months_passed(2018, 11, 1) == 0


def test_nine_days_later():
    assert calc_months_passed(2018, 11, 10) == 0


def test_ten_days_later():
    assert calc_months_passed(2018, 11, 11) == 1


def test_one_month_and_nine_days_later():
    assert calc_months_passed(2018, 12, 10) == 1


def test_one_month_and_ten_day_later():
    assert calc_months_passed(2018, 12, 11) == 2


def test_one_year_one_month_and_nine_days_later():
    assert calc_months_passed(2019, 12, 10) == 13


def test_one_year_one_month_and_ten_days_later():
    assert calc_months_passed(2019, 12, 11) == 14


def test_non_int_input_args():
    with pytest.raises(TypeError):
        calc_months_passed('a', 10, 1)
    with pytest.raises(TypeError):
        calc_months_passed(2018, 'b', 1)
    with pytest.raises(TypeError):
        calc_months_passed(2018, 10, 'c')


def test_out_of_dt_range_args():
    with pytest.raises(ValueError):
        calc_months_passed(-1000, 11, 1)
    with pytest.raises(ValueError):
        calc_months_passed(2018, 13, 1)
    with pytest.raises(ValueError):
        calc_months_passed(2018, 11, 34)


def test_new_date_in_past_raises_value_error():
    with pytest.raises(ValueError):
        calc_months_passed(2018, 10, 1)