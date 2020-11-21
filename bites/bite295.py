'''
Bite295: Join Lists
Write a function that accepts a list of lists and joins them with a separator character, therefore flattening and separating.  
'''
from typing import List, Union
import functools

# new_lst = list()
def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    if lst_of_lst == []:
        return None
        
    result = functools.reduce(lambda x, y: x + [sep] + y, lst_of_lst)
    return result
    # for lst in lst_of_lst:
    #     new_lst.extend(lst + [sep])
    # return new_lst[:-1]
    
    
# tests

import pytest

from join_lists import join_lists


@pytest.mark.parametrize('input_list, sep, expected', [
                        ([], '&', None),
                        ([['a']], '|', ['a']),
                        ([['a', 'b']], '&', ['a', 'b']),
                        ([['a', 'b'], ['c']], '&', ['a', 'b', '&', 'c']),
                        ([['a', 'b'], ['c'], ['d', 'e']], '+',
                         ['a', 'b', '+', 'c', '+', 'd', 'e']),
])
def test_join_lists(input_list, sep, expected):
    assert join_lists(input_list, sep) == expected