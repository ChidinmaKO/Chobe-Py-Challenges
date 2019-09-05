import requests
import json

YOUR_KEY = '123abc'
DEFAULT_LIST = 'hardcover-nonfiction'

URL_NON_FICTION = (f'https://api.nytimes.com/svc/books/v3/lists/current/'
                   f'{DEFAULT_LIST}.json?api-key={YOUR_KEY}')
URL_FICTION = URL_NON_FICTION.replace('nonfiction', 'fiction')


def get_best_seller_titles(url=URL_NON_FICTION):
    """Use the NY Times Books API endpoint above to get the titles that are
       on the best seller list for the longest time.

       Return a list of (title, weeks_on_list) tuples, e.g. for the nonfiction:

       [('BETWEEN THE WORLD AND ME', 86),
        ('EDUCATED', 79),
        ('BECOMING', 41),
        ('THE SECOND MOUNTAIN', 18),
         ... 11 more ...
       ]

       Dev docs: https://developer.nytimes.com/docs/books-product/1/overview
    """
    with requests.Session() as request:
        response = request.get(url)
    try:
        data = response.json()
    except json.JSONDecodeError:
        print(f"JSON Decode Error")
    outcome = data['results']['books']
        
    # result = [(book['title'], book['weeks_on_list']) for book in outcome]
    
    # sorted_result = sorted(result, key=lambda result: result[1], reverse=True)
    # return sorted_result
    
    sorted_weeks = sorted(outcome, key=lambda outcome: outcome['weeks_on_list'], reverse=True)
    
    title_week_tuple = [(book['title'], book['weeks_on_list']) for book in sorted_weeks]
    return title_week_tuple


if __name__ == '__main__':
    ret = get_best_seller_titles()
    print(ret)


# tests
import json
from pathlib import Path
from unittest.mock import patch
from urllib.request import urlretrieve

# from nyt import (get_best_seller_titles, URL_NON_FICTION, URL_FICTION)

TMP = Path('/tmp')

FICTION = TMP / 'nyt-fiction.json'
if not FICTION.exists():
    urlretrieve('https://bit.ly/2L7S5zz', FICTION)

NON_FICTION = TMP / 'nyt-nonfiction.json'
if not NON_FICTION.exists():
    urlretrieve('https://bit.ly/2LhVvyr', NON_FICTION)


def mocked_requests_get(*args, **kwargs):
    """https://stackoverflow.com/a/28507806"""

    class MockResponse:

        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    url = args[0]
    fname = NON_FICTION if 'nonfiction' in url else FICTION
    with open(fname) as f:
        return MockResponse(json.loads(f.read()), 200)

    return MockResponse(None, 404)


@patch('requests.get', side_effect=mocked_requests_get)
def test_response_nonfiction(mock_get):
    assert get_best_seller_titles(url=URL_NON_FICTION) == [
        ('BETWEEN THE WORLD AND ME', 86),
        ('EDUCATED', 79),
        ('BECOMING', 41),
        ('THE SECOND MOUNTAIN', 18),
        ('THE PIONEERS', 16),
        ('MAYBE YOU SHOULD TALK TO SOMEONE', 14),
        ('UNFREEDOM OF THE PRESS', 14),
        ('RANGE', 9),
        ('THREE WOMEN', 7),
        ('TRICK MIRROR', 3),
        ('HOW TO BE AN ANTIRACIST', 2),
        ('KOCHLAND', 2),
        ('THANK YOU FOR MY SERVICE', 1),
        ('THE OUTLAW OCEAN', 1),
        ('GODS OF THE UPPER AIR', 1)
    ]


@patch('requests.get', side_effect=mocked_requests_get)
def test_response_fiction(mock_get):
    assert get_best_seller_titles(url=URL_FICTION) == [
        ('WHERE THE CRAWDADS SING', 51),
        ('THE SILENT PATIENT', 25),
        ('EVVIE DRAKE STARTS OVER', 7),
        ('THE NICKEL BOYS', 6),
        ('ASK AGAIN, YES', 6),
        ('ONE GOOD DEED', 5),
        ('THE INN', 3),
        ('THE TURN OF THE KEY', 3),
        ('OUTFOX', 3),
        ('THE BITTERROOTS', 2),
        ('INLAND', 2),
        ('OLD BONES', 1),
        ('THE LAST WIDOW', 1),
        ('THE WHISPER MAN', 1),
        ('TIDELANDS', 1)
    ]