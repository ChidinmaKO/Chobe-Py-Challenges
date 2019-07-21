# https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php

#6. Write a Python program to get the sum of a non-negative integer

# using for-loop 
def func(nums):
    total = 0
    if nums < 1:
        raise ValueError("Number less than zero")
    else:
        num = list(map(int, str(nums)))
        for n in num:
            total += n
        return total


# using recursion
def func(nums):
    if nums < 1:
        return 0
    else:
        return func(nums // 10) + (nums % 10)