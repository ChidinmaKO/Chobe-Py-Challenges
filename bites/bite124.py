from collections import namedtuple, Counter
import csv
import re

import requests
from typing import List, Tuple


MARVEL_CSV = 'https://raw.githubusercontent.com/pybites/marvel_challenge/master/marvel-wikia-data.csv'  # noqa E501

Character = namedtuple('Character', 'pid name sid align sex appearances year')

min_max = Tuple[str, str]


# csv parsing code provided so this Bite can focus on the parsing

def _get_csv_data():
    """Download the marvel csv data and return its decoded content"""
    with requests.Session() as session:
        return session.get(MARVEL_CSV).content.decode('utf-8')
        

def load_data():
    """Converts marvel.csv into a sequence of Character namedtuples
       as defined above"""
    content = _get_csv_data()
    reader = csv.DictReader(content.splitlines(), delimiter=',')
    for row in reader:
        name = re.sub(r'(.*?)\(.*', r'\1', row['name']).strip()
        yield Character(pid=row['page_id'],
                        name=name,
                        sid=row['ID'],
                        align=row['ALIGN'],
                        sex=row['SEX'],
                        appearances=row['APPEARANCES'],
                        year=row['Year'])


characters = list(load_data())

def most_popular_characters(data=characters, top:int = 5) -> List[str]:
    """Get the most popular character by number of appearances,
       return top n characters (default 5)"""
    popular_char = [(datum.name, int(datum.appearances)) for datum in data if datum.appearances]
    sorted_ = sorted(popular_char, key=lambda popular_char: popular_char[1], reverse=True)[:top]
    result = [r[0] for r in sorted_]
    return result
    

def max_and_min_years_new_characters(data=characters) -> min_max:
    """Get the year with most and least new characters introduced respectively,
       use either the 'FIRST APPEARANCE' or 'Year' column in the csv data, or
       the 'year' attribute of the namedtuple, return a tuple of
       (max_year, min_year)"""
    char_per_year = Counter(char.year for char in data if char.year)
    max_year = char_per_year.most_common(1)[0][0]
    min_year = char_per_year.most_common()[-1][0]
    return max_year, min_year


def get_percentage_female_characters(data=characters) -> int:
    """Get the percentage of female characters as percentage of all genders over
       all appearances, rounded to 2 digits"""
    all_char = Counter(char.sex for char in data if char.sex)
    female_char = all_char['Female Characters']
    total = sum(all_char.values())
    result = round((female_char/total) * 100, 2)
    return result

# tests
from marvel import (characters,
                    most_popular_characters,
                    max_and_min_years_new_characters,
                    get_percentage_female_characters)

half_size = int(len(characters)/2)

half_characters = characters[:half_size]


def test_most_popular_characters():
    actual = most_popular_characters()
    expected = ['Spider-Man', 'Captain America', 'Wolverine',
                'Iron Man', 'Thor']
    assert actual == expected


def test_max_and_min_years_new_characters():
    actual = max_and_min_years_new_characters()
    expected = ('1993', '1958')
    assert actual == expected


def test_get_percentage_female_characters():
    actual = get_percentage_female_characters()
    expected = 24.72
    assert actual == expected


def test_most_popular_characters_smaller_data_set_and_top_2():
    expected = ['Spider-Man', 'Captain America']
    actual = most_popular_characters(half_characters, top=2)
    assert actual == expected


def test_max_and_min_years_new_characters_smaller_data_set():
    expected = ('1992', '1959')
    actual = max_and_min_years_new_characters(half_characters)
    assert actual == expected


def test_get_percentage_female_characters_smaller_data_set():
    actual = get_percentage_female_characters(half_characters)
    expected = 28.73
    assert actual == expected