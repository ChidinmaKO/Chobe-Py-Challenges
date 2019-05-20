import calendar
from datetime import date


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    get_weekday = date.weekday()
    weekday = calendar.day_name[get_weekday]
    return weekday