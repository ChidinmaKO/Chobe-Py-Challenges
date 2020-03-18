# iterators, random

from random import choice
from dataclasses import dataclass

COLORS = 'red blue green yellow brown purple'.split()

@dataclass
class EggCreator:
    limit: int
    
    def __post_init__(self):
        self.index = 0
    
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.index >= self.limit:
            raise StopIteration
        suffix = ' egg'
        self.index += 1
        return choice(COLORS) + suffix


# tests
import pytest

from eggs import EggCreator, COLORS


def test_iterator_type():
    eg = EggCreator(10)
    assert type(eg) == EggCreator


def test_len_iterator_is_limit_input_arg():
    ec = EggCreator(2)
    assert len(list(ec)) == 2
    ec = EggCreator(5)
    assert len(list(ec)) == 5


def test_call_next_on_iterator():
    ec = EggCreator(2)
    next_egg = next(ec)
    assert next_egg.split()[0] in COLORS


def test_iterator_raises_stop_iteration_exception():
    ec = EggCreator(2)
    next(ec)
    next(ec)
    with pytest.raises(StopIteration):
        next(ec)


def test_iterator_generates_random_colors():
    ec = EggCreator(20)
    output1 = list(ec)
    ec = EggCreator(20)
    output2 = list(ec)
    assert output1 != output2