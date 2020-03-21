# OrderedDict
from collections import OrderedDict

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()
HONORS = OrderedDict(zip(scores, belts))
MIN_SCORE, MAX_SCORE = min(scores), max(scores)

# One way
def get_belt(user_score: int):
    result = ''
    
    if user_score < MIN_SCORE:
        return None
    if user_score > MAX_SCORE:
        return belts[-1]
    
    for k,v in HONORS.items():
        if user_score >= k:
            result = v
    return result

# Another way using OrderedDict && Itertools
def get_belt(user_score: int):
    if user_score < MIN_SCORE:
        return None
    if user_score > MAX_SCORE:
        return belts[-1]
        
    result = list(takewhile(lambda x: x[0] <= user_score, HONORS.items()))
    return result[-1][1]


# TESTS
import pytest

from belt import get_belt


@pytest.mark.parametrize("input_argument, expected_return", [
    (0, None),
    (9, None),
    (10, 'white'),
    (48, 'white'),
    (50, 'yellow'),
    (101, 'orange'),
    (249, 'green'),
    (250, 'blue'),
    (251, 'blue'),
    (400, 'brown'),
    (599, 'brown'),
    (600, 'black'),
    (788, 'black'),
    (800, 'paneled'),
    (999, 'paneled'),
    (1000, 'red'),
    (1200, 'red'),
])
def test_get_belt(input_argument, expected_return):
    assert get_belt(input_argument) == expected_return