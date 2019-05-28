from string import punctuation

def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    # first way
    # remove = set(punctuation)
    # new_str = ''.join([char for char in input_string if char not in remove])
    # return new_str
    
    # second way
    # table = input_string.translate(str.maketrans('', '', punctuation))
    # return table
    
    # third way
    # table2 = input_string.translate(str.maketrans({key: None for key in punctuation}))
    # return table2
    
    # fourth way
    table3 = input_string.translate(str.maketrans(dict.fromkeys(punctuation)))
    return table3



# tests

import pytest

from clean import remove_punctuation


@pytest.mark.parametrize("input_argument, expected_return", [
    ('Hello, I am Tim.', 'Hello I am Tim'),
    (';String. with. punctuation characters!',
     'String with punctuation characters'),
    ('Watch out!!!', 'Watch out'),
    ('Spaces - should - work the same, yes?',
     'Spaces  should  work the same yes'),
    ("Some other (chars) |:-^, let's delete them",
     'Some other chars  lets delete them'),
])
def test_remove_punctuation(input_argument, expected_return):
    assert remove_punctuation(input_argument) == expected_return