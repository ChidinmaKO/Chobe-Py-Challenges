'''
Bite 270: Most frequent digit in number
Given an integer number, find the most frequent digit in it.

Examples:

1998 -> two 9's, one 1, one 8 so return 9
177 -> return 7
2020 -> there is 2 two's, 2 zero's. Return 2 = the first highest hitter
12345 -> all digits occur once, so like the last example return the first digit = 1

'''
from collections import Counter

def freq_digit(num: int) -> int:
    # convert to str
    num_str = str(num)
    most_common = Counter(num_str).most_common(1)[0][0]
    # convert back to int
    return int(most_common)
