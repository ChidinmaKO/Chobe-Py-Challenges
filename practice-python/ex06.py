user_input = input("give me a string: ")

if user_input == user_input[::-1]:
  print(f"{user_input} is a palindrome")
else:
  print(f"{user_input}is Not a palindrome")