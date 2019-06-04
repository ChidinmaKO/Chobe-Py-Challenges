birthdays= {
  "Chidinma Doe": "10/10/1994",
  "Ezinne Tobi": "13/10/1996",
  "Ada Precious": "12/10/1999",
  "Joe Ola": "18/10/1990"
}
print("Welcome to the birthday dictionary. We know the birthdays of: ")
for k in birthdays.keys():
  print(k)
print("Who's birthday do you want to look up?")
name = input("Give me a name: ")
result = birthdays.get(name.title(), "not available")
print(f"{name.title()}'s birthday is {result}")