def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    # one way
    # counts = text.rstrip().count(' ') if text.startswith(' ') else 0
    # return counts
    
    # another way
    counts = len(text) - len(text.lstrip())
    return counts

# tests

# import pytest

@pytest.mark.parametrize("input_string, count", [
   ('string  ', 0),
   ('  string', 2),
   ('    string', 4),
   ('            string', 12),
])
def test_count_indents(input_string, count):
    assert count_indents(input_string) == count