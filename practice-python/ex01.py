from datetime import datetime as dt

name = str(input("What's your name? "))
age = int(input("What's your age? "))
num = int(input("Give me a random number: "))
year = dt.now().year

age_100 = year + (100 - age)
print(f"You'll be 100 years old in year {age_100} \n" * num)