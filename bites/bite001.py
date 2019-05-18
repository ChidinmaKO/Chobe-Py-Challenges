def sum_numbers(numbers=None):
    number_sum = 0
    if numbers is None:
        for num in range(1,101):
          number_sum += num
        return number_sum
    else:
        for nums in numbers:
          number_sum += nums
        return number_sum

# Better way
def sum_numbers(numbers=None):
  if numbers is None:
    numbers = range(1,101)
  print(sum(numbers))