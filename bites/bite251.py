import string

import pandas as pd


def basic_series() -> pd.Series:
    """Create a pandas Series containing the values 1, 2, 3, 4, 5
    Don't worry about the indexes for now.
    The name of the series should be 'Fred'
    """
    series = pd.Series(range(1,6), name="Fred")
    return series


def float_series() -> pd.Series:
    """Create a pandas Series containing the all the values
    from 0.000 -> 1.000 e.g. 0.000, 0.001, 0.002... 0.999, 1.000
    Don't worry about the indexes or the series name.
    """
    series = pd.Series([(n/1000) for n in range(1001)])
    return series


def alpha_index_series() -> pd.Series:
    """Create a Series with values 1, 2, ... 25, 26 of type int64
    and add an index with values a, b, ... y, z
    so index 'a'=1, 'b'=2 ... 'y'=25, 'z'=26
    Don't worry about the series name.
    """
    series = pd.Series(data=range(1,27), index=list(string.ascii_lowercase))
    return series


def object_values_series() -> pd.Series:
    """Create a Series with values A, B, ... Y, Z of type object
    and add an index with values 101, 102, ... 125, 126
    so index 101='A', 102='B' ... 125='Y', 126='Z'
    Don't worry about the series name.
    """
    series = pd.Series(data=list(string.ascii_uppercase), index=range(101,127))
    return series

# tests
import string

import pandas as pd

import series as se


def test_basic_series():
    ser = se.basic_series()
    assert isinstance(ser, pd.Series)
    assert ser.name == "Fred"
    assert ser.dtype == "int64"
    assert all(n in [1, 2, 3, 4, 5] for n in ser.values)


def test_floats_series():
    ser = se.float_series()
    assert isinstance(ser, pd.Series)
    assert ser.dtype == "float64"
    assert len(ser) == 1001
    assert ser.sum() == 500.5


def test_alpha_index_series():
    ser = se.alpha_index_series()
    assert isinstance(ser, pd.Series)
    assert ser.dtype == "int64"
    assert len(ser) == 26
    assert sum(ser.values) == 351
    assert all(c in string.ascii_lowercase for c in ser.index)


def test_object_values_series():
    ser = se.object_values_series()
    assert isinstance(ser, pd.Series)
    assert len(ser) == 26
    assert all(c in string.ascii_uppercase for c in ser.values)
    assert ser[101] == "A"
    assert ser[126] == "Z"