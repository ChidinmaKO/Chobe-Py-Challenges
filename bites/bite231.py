import re
from typing import List

# https://stackoverflow.com/a/43147265
# just for exercise sake, real life use emoji lib
IS_EMOJI = re.compile(r'[^\w\s,]')


def get_emoji_indices(text: str) -> List[int]:
    """Given a text return indices of emoji characters"""
    # long way
    # t = re.findall(IS_EMOJI, text)

    # result = [index for index in enumerate(text) if index[1] in t]
    # p = [i[0] for i in result]
    # return p
    
    # shorter way
    # result = [index for index, char in enumerate(text) if IS_EMOJI.match(char)]
    # return result
    
    # another smart apporach
    pattern = IS_EMOJI.finditer(text)
    result = [index.start() for index in pattern]
    return result

# tests
import pytest

# from emojis import get_emoji_indices


@pytest.mark.parametrize("emojis, expected", [
    ('We 💜 Python 🐍', [3, 12]),
    ('We are so happy 😊😍 seeing you all coding', [16, 17]),
    ('😂 ROFL that is funny 😂', [0, 21]),
    ('No way 😭, that is not cool 🤔', [7, 27]),
    ('Great job 👌 hitting that Ninja 💪 belt', [10, 31]),
    ('Good luck with your 100 days of code 💯', [37]),
    ('Our 🥋 ninjas are on fire 🔥', [4, 25]),
    ('Happy Valentine 💕, buy some gifts 🎁', [16, 34]),
    ('pytest is so cool 😎, after grasping it 🤯', [18, 39]),
    ('Books can be boring 😴, better to code 💪❗', [20, 38, 39]),
])
def test_get_emoji_indices(emojis, expected):
    assert get_emoji_indices(emojis) == expected