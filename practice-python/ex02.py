num = int(input("Give me a number: "))
check = int(input("Give me a divisor: "))
if num % 2 == 0:
  print(f"{num} is even")
  if num % 4 == 0:
    print(f"{num} is a multiple of 4")
else:
  print(f"{num} is odd")


if num % check == 0:
  print(f"{num} is divisible by {check}")
else:
  print(f"{num} is NOT divisible by {check}")