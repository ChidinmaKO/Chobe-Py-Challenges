import re
import string


def password_complexity(password):
    """Input: password string, calculate score according to 5 criteria in bite,
       return: score int"""
    score = 0
    lowercase = re.search("[a-z]+", password)
    uppercase = re.search("[A-Z]+", password)
    numbers = re.search("[0-9]+", password)
    special_chars = re.search(r'[' + re.escape(string.punctuation) + ']', password)
    length = len(password.strip())
    repetition = re.search(r"([\w\W])\1{1,}", password)
    
    if lowercase or uppercase:
        score = 0
    if lowercase and uppercase:
        score += 1
    if (lowercase or uppercase) and numbers:
        score += 1
    if special_chars:
        score += 1
    if length >= 8:
        score += 1
        if not repetition:
          score += 1

    return score

# tests
import pytest

from password import password_complexity


@pytest.mark.parametrize("arg, expected", [
    ('abc', 0),
    ('ABC', 0),
    ('123', 0),
    ('abc1', 1),
    ('ABC1', 1),
    ('@', 1),
    ('aA@', 2),
    ('aA1@', 3),
    ('aA1@1224', 4),  # repeated 2
    ('aA1@1234', 5),
    ('aaaabbbbc', 1),
    ('abcdabcd', 2),
    ('Abcdabcd', 3),
    ('Abcdabc$', 4),
    ('Abcdab1$', 5),
    ('Abcdaac$', 3),
    ('123$abc', 2),
    ('123$abC', 3),
    ('123$abcd', 4),
    ('123$abC1', 5),
    ('123$abb1', 3),
    ('123$Abb1', 4),
    ('123$Abc1', 5),
    ('@@@@@@@@@@', 2),
    ('@$@$@$@$@$', 3),
])
def test_password_complexity(arg, expected):
    assert password_complexity(arg) == expected