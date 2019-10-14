from random import random
from time import sleep
from functools import wraps


def cached_property(func):
    """decorator used to cache expensive object attribute lookup"""
    cache = {}
    
    @property
    # @wraps(func)
    def _cached(*args, **kwargs):
        key = 0
        if key not in cache:
            cache[key] = func(*args, **kwargs)
            return cache[key]
        else:
            return cache[key]
    return _cached

class Planet:
    """the nicest little orb this side of Orion's Belt"""

    GRAVITY_CONSTANT = 42
    TEMPORAL_SHIFT = 0.12345
    SOLAR_MASS_UNITS = 'M\N{SUN}'

    def __init__(self, color):
        self.color = color
        self._mass = None

    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self.color)})'

    # @property
    @cached_property
    def mass(self):
        scale_factor = random()
        sleep(self.TEMPORAL_SHIFT)
        self._mass = (f'{round(scale_factor * self.GRAVITY_CONSTANT, 4)} '
                      f'{self.SOLAR_MASS_UNITS}')
        return self._mass

    # @mass.setter
    # def mass(self, value):
    #     self._mass = value

# tests
from time import perf_counter
import pytest

from cached_property import Planet


@pytest.fixture(scope="module")
def blue():
    return Planet('blue')


def test_property_is_cached_timing(blue):
    start_time = perf_counter()
    for _ in range(5):
        blue.mass
    end_time = perf_counter()
    elapsed_time = end_time - start_time
    assert elapsed_time < .5


def test_property_is_cached_value(blue):
    masses = [blue.mass for _ in range(10)]
    initial_mass = masses[0]
    assert all(m == initial_mass for m in masses)


def test_property_is_immutable(blue):
    with pytest.raises(AttributeError):
        blue.mass = 11
