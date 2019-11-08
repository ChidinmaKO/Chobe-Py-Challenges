import re
import shlex

def split_words_and_quoted_text(text):
    """Split string text by space unless it is
       wrapped inside double quotes, returning a list
       of the elements.

       For example
       if text =
       'Should give "3 elements only"'

       the resulting list would be:
       ['Should', 'give', '3 elements only']
    """
    # using shlex
    # return shlex.split(text)
    
    # using re
    result = list()
    pattern = re.findall(r'\w+\s*|\".+?\"', text)
    for char in pattern:
        result.append(char.strip().replace('"', ''))
    return result
        

# tests
import pytest

from split import split_words_and_quoted_text

some_strings = (
    'Should give "3 words only"',
    'Our first program was "Hello PyBites"',
    'Because "Hello World" is really cliche',
    ('PyBites is a "A Community that Masters '
     'Python through Code Challenges"')
)
expected_returns = (
    ['Should', 'give', '3 words only'],
    ['Our', 'first', 'program', 'was', 'Hello PyBites'],
    ['Because', 'Hello World', 'is', 'really', 'cliche'],
    ['PyBites', 'is', 'a', ('A Community that Masters Python '
                            'through Code Challenges')]
)


@pytest.mark.parametrize("arg, ret",
                         zip(some_strings, expected_returns))

def test_split_words_and_quoted_text(arg, ret):
    assert split_words_and_quoted_text(arg) == ret