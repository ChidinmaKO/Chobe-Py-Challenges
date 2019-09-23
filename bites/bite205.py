from urllib.request import urlretrieve
from pathlib import Path

import gender_guesser.detector as gender
from bs4 import BeautifulSoup as Soup

import re
import collections

TMP = Path('/tmp')
PYCON_HTML = TMP / "pycon2019.html"
if not PYCON_HTML.exists():
    urlretrieve('https://bit.ly/2O5Bik7', PYCON_HTML)


def _get_soup(html=PYCON_HTML):
    return Soup(html.read_text(encoding="utf-8"), "html.parser")


def get_pycon_speaker_first_names(soup=None):
    """Parse the PYCON_HTML using BeautifulSoup, extracting all
       speakers (class "speaker"). Note that some items contain
       multiple speakers so you need to extract them.
       Return a list of first names
    """
    if soup is None:
        soup = _get_soup(PYCON_HTML)
        
    all_speakers = soup.find_all('span', class_='speaker')
    speaker_names = [names.strip() for speakers in all_speakers for names in re.split('[,/]', speakers.text.strip())]
    result = [name.split()[0] for name in speaker_names]
    return result


def get_percentage_of_female_speakers(first_names):
    """Run gender_guesser on the names returning a percentage
       of female speakers, rounded to 2 decimal places."""
    detector = gender.Detector(case_sensitive = False)
    
    gender_count = collections.Counter([detector.get_gender(names) for names in first_names])
    
    female_percentage = ((gender_count['female'] + gender_count['mostly_female']) / len(first_names)) * 100
    
    return round(female_percentage, 2)


if __name__ == '__main__':
    names = get_pycon_speaker_first_names()
    perc = get_percentage_of_female_speakers(names)
    print(perc)

# tests

import pytest

# from speaker import (get_pycon_speaker_first_names, get_percentage_of_female_speakers)


@pytest.fixture(scope='module')
def first_names():
    return get_pycon_speaker_first_names()


def test_get_pycon_speaker_first_names(first_names):
    assert len(first_names) == 112
    assert 'Luciano' in first_names
    assert 'Erin' in first_names
    assert 'Rachael' in first_names


def test_get_percentage_of_female_speakers(first_names):
    actual = get_percentage_of_female_speakers(first_names)
    expected = 28.57
    assert actual == expected