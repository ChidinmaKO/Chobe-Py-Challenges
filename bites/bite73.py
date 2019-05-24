import pytz
from datetime import datetime

MEETING_HOURS = range(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc, *timezones):
    """Receive a utc datetime and one or more timezones and check if
       they are all within schedule (MEETING_HOURS)"""
    aware_utc = utc.replace(tzinfo=pytz.UTC)

    for tz in timezones:
        if not (tz in TIMEZONES):
            raise ValueError("Timezone isn't valid")
        localhour = aware_utc.astimezone(pytz.timezone(tz)).hour
        if not(localhour in MEETING_HOURS):
            return False
    return True