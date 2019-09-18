from collections import defaultdict
import os
from urllib.request import urlretrieve

from bs4 import BeautifulSoup


# prep data
holidays_page = os.path.join('/tmp', 'us_holidays.php')
urlretrieve('https://bit.ly/2LG098I', holidays_page)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    soup = BeautifulSoup(content, 'html.parser')
    table_rows = soup.select('table.list-table tr')
    
    for table_row in table_rows:
        try:
            date = table_row.find('time').get('datetime')
            month = date.split("-")[1]
            holiday = table_row.find('a').text
        except Exception:
            pass
        else:
            holidays[month].append(holiday)
    return holidays

# tests
import pytest

from holidays import get_us_bank_holidays


holidays = get_us_bank_holidays()


@pytest.mark.parametrize("month, holiday", [
    ('01', ["New Year's Day", 'Martin Luther King Jr. Day ']),
    ('02', ["Presidents' Day"]),
    ('04', ['Emancipation Day']),
    ('05', ["Mother's Day", 'Memorial Day ']),
    ('06', ["Father's Day"]),
    ('07', ['Independence Day ']),
    ('09', ['Labor Day ']),
    ('10', ['Columbus Day ']),
    ('11', ['Veterans Day ', 'Thanksgiving', 'Day after Thanksgiving ']),
    ('12', ['Christmas Day']),
])
def test_get_us_bank_holidays(month, holiday):
    assert holidays.get(month) == holiday