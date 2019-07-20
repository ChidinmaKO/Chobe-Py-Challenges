# https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php

# 1. Write a Python program to calculate the sum of a list of numbers

list1 = [4,5,6,7,2,9]
print(sum(list1))

# using for loop 
# def sumfunc(list1):
#   sum_list = 0
#   for num in list1:
#     sum_list += num
#   return sum_list


# using recursion
def sumfunc(list1):
  if len(list1) == 1:
    return list1[0]
  else:
    return list1[0] + sumfunc(list1[1:])

sumfunc(list1)