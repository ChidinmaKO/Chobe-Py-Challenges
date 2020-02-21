import numpy as np
import pandas as pd


def return_at_index(ser: pd.Series, idx: int) -> object:
    """Return the Object at the given index of the Series
    If you want to be extra careful catch and raise an error if
       the index does not exist.
    """
    try:
        result = ser.iloc[idx]
    except:
        pass
    return result


def get_slice(ser: pd.Series, start: int, end: int) -> pd.core.series.Series:
    """Return the slice of the given Series in the range between
    start and end.
    """
    return ser.iloc[start:end]


def get_slice_inclusive(ser: pd.Series,
                        start: int, end: int) -> pd.core.series.Series:
    """Return the slice of the given Series in the range between
    start and end inclusive.
    """
    return ser.iloc[start:end+1]


def return_head(ser: pd.Series, num: int) -> pd.core.series.Series:
    """Return the first num elements of the given Series.
    """
    return ser.head(num)


def return_tail(ser: pd.Series, num: int) -> pd.core.series.Series:
    """Return the last num elements of the given Series.
    """
    return ser.tail(num)


def get_index(ser: pd.Series) -> pd.core.indexes.base.Index:
    """Return all indexes of the given Series.
    """
    return ser.index


def get_values(ser: pd.Series) -> np.ndarray:
    """Return all the values of the given Series.
    """
    return ser.values


def get_every_second_indexes(ser: pd.Series,
                             even_index=True) -> pd.core.series.Series:
    """Return all rows where the index is either even or odd.
    If even_index is True return every index where idx % 2 == 0
    If even_index is False return every index where idx % 2 != 0
    Assume default indexing i.e. 0 -> n
    """
    idx = 0 if even_index else 1
    return ser.iloc[idx::2]



# tests
import inspect
import string

import pytest
import numpy as np
import pandas as pd

import series as se


@pytest.fixture()
def float_series():
    """Returns a pandas Series containing floats"""
    return pd.Series([float(n) / 1000 for n in range(0, 1001)])


@pytest.fixture()
def alpha_series():
    """Returns a pandas Series containing floats"""
    dictionary = dict(zip(string.ascii_lowercase, range(1, 27)))
    return pd.Series(dictionary)


@pytest.mark.parametrize("arg, expected", [
    (0, 0.000), (500, 0.500), (1000, 1.000)
])
def test_return_at_index(float_series, arg, expected):
    assert se.return_at_index(float_series, arg) == expected


def test_return_at_index_raise_exception(float_series):
    with pytest.raises(KeyError):
        float_series[1111]


def test_get_slice(float_series):
    slce = se.get_slice(float_series, 20, 25)
    assert isinstance(slce, pd.core.series.Series)
    assert len(slce) == 5
    assert slce[24] == 0.024


def test_get_slice_inclusive(float_series):
    slce = se.get_slice_inclusive(float_series, 20, 25)
    assert isinstance(slce, pd.core.series.Series)
    assert len(slce) == 6
    assert slce[25] == 0.025


@pytest.mark.parametrize("arg, expected", [
    (0, 0.000), (5, 0.005), (9, 0.009)
])
def test_return_head(float_series, arg, expected):
    assert se.return_head(float_series, 10)[arg] == expected
    assert ".head" in inspect.getsource(se.return_head)


@pytest.mark.parametrize("arg, expected", [
    (991, 0.991), (995, 0.995), (1000, 1.000)
])
def test_return_tail(float_series, arg, expected):
    assert se.return_tail(float_series, 10)[arg] == expected
    assert ".tail" in inspect.getsource(se.return_tail)


def test_get_index(alpha_series):
    idx = se.get_index(alpha_series)
    assert isinstance(idx, pd.core.indexes.base.Index)
    assert len(idx) == 26
    assert all(c in string.ascii_lowercase for c in idx.values)
    assert ".index" in inspect.getsource(se.get_index)


def test_get_values(alpha_series):
    vals = se.get_values(alpha_series)
    assert isinstance(vals, np.ndarray)
    assert len(vals) == 26
    assert all(c in range(1, 27) for c in vals)


def test_all_even_indexes_returned(float_series):
    ser = se.get_every_second_indexes(float_series, True)
    assert all(n % 2 == 0 for n in ser.index)
    assert round(sum(ser), 1) == 250.5


def test_all_odd_indexes_returned(float_series):
    ser = se.get_every_second_indexes(float_series, False)
    assert all(n % 2 == 1 for n in ser.index)
    assert round(sum(ser), 1) == 250.0