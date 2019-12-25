import random

BITES = {6: 'PyBites Die Hard',
         7: 'Parsing dates from logs',
         9: 'Palindromes',
         10: 'Practice exceptions',
         11: 'Enrich a class with dunder methods',
         12: 'Write a user validation function',
         13: 'Convert dict in namedtuple/json',
         14: 'Generate a table of n sequences',
         15: 'Enumerate 2 sequences',
         16: 'Special PyBites date generator',
         17: 'Form teams from a group of friends',
         18: 'Find the most common word',
         19: 'Write a simple property',
         20: 'Write a context manager',
         21: 'Query a nested data structure'}
bites_done = {6, 10, 16, 18, 21}


class NoBitesAvailable(Exception):
    pass


class Promo:

    def __init__(self, bites_done=bites_done):
        self.bites_done = bites_done

    def _pick_random_bite(self):
        try:
            available_bites = random.choice(list(BITES.keys() - self.bites_done))
        except:
            raise NoBitesAvailable
        else:
            return available_bites

    def new_bite(self):
        mint_bite = self._pick_random_bite()
        self.bites_done.add(mint_bite)
        return mint_bite



# tests
import inspect
from unittest.mock import patch

import pytest

from promo import (Promo, NoBitesAvailable,
                   BITES, bites_done)

BITES_AVAILABLE = len(BITES) - len(bites_done)


def grab_bites(promo, amount=BITES_AVAILABLE):
    # _ is a throw-away variable (just want a loop)
    for _ in range(amount):
        promo.new_bite()


@pytest.fixture
def promo():
    """Make a fresh new promo object for each test"""
    return Promo(bites_done=bites_done.copy())


def test_bites_not_done_start(promo):
    assert len(BITES) == 15
    assert len(promo.bites_done) == 5


@patch('random.choice', side_effect=[7, 9, 11])
@patch('random.sample', side_effect=[[7], [9], [11]])
def test_new_bite(choice_mock, sample_mock, promo):
    assert promo.new_bite() == 7
    assert promo.new_bite() == 9
    assert promo.new_bite() == 11


def test_random_is_used(promo):
    src = inspect.getsource(promo._pick_random_bite)
    assert 'sample' in src or 'choice' in src


def test_pick_random_bite_returns_not_done_bite(promo):
    for _ in range(10):
        bite = promo._pick_random_bite()
        assert type(bite) == int
        assert bite in BITES
        assert bite not in promo.bites_done


def test_internal_data_structures(promo):
    # fixture = new data = start over
    assert len(promo.bites_done) == 5
    grab_bites(promo, amount=7)
    # bites_done incremented with 7
    assert len(promo.bites_done) == 12


def test_raise_exception_if_no_more_bites(promo):
    assert len(promo.bites_done) == 5
    grab_bites(promo)
    # exhausted bites
    with pytest.raises(NoBitesAvailable):
        promo._pick_random_bite()