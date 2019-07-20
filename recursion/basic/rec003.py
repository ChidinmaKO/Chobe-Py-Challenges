# https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php

#4. Write a Python program to get the factorial of a non-negative integer
def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)