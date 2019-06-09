def req():
  user = input("give me a sentence: ")
  split_str = user.split()
  print(' '.join(split_str[::-1]))

req()