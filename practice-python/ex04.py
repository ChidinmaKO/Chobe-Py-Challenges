num = int(input("Give me a num: "))

div = []

for i in range(1, (num+1)):
  if num % i == 0:
    div.append(i)
print(div)