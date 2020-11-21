'''
Bite 278: Major and minor numbers
You are given a list of integers. Write code to find the majority and minorty numbers in that list.
'''
from collections import Counter
def major_n_minor(numbers):
    """
    Input: an array with integer numbers
    Output: the majority and minority number
    """
    
    count_ = Counter(numbers)

    major = max(count_, key=count_.get)
    minor = min(count_, key=count_.get)
    
    return major, minor