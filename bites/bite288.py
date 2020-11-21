'''
Write a function that accepts a list of digits and returns the smallest number that can be created by combining unique digits.

Therefore, you have to ignore duplicated digits.  

Examples:  

[1] => 1

[7, 1] => 17  

[1, 9, 5, 9, 1] => 159

Note: An empty input list [] should return 0.
'''

from typing import List


def minimum_number(digits: List[int]) -> int:
    if len(digits) == 0:
        return 0
    else:
        return int(''.join(str(i) for i in sorted(set(digits))))
