# https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php

#3. Write a Python program of recursion list sum

test = [1, 2, [3,4], [5,6]]

# using for loop
def func0(test):
    total = 0
    for num in test:
        if type(num) == int:
            total += num
        else:
            for i in num:
                total += i
    return total

# using recursion
def func1(test):
    total = 0
    if len(test) == 1:
        return test[0]
    else:
        for num in test:
            if not isinstance(num, list):
                total += num
            else:
                total += func1(num)
        return total

# using recursion + comprehension

def func2(test):
    if len(test) == 1:
        return test[0]
    else:
        return sum((num if not isinstance(num, list) else func2(num) for num in test), 0)