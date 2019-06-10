from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import random

zipped = ascii_lowercase + ascii_uppercase + digits + punctuation

user = input("Do you want a strong password? Y/N ")

passlen = 8 if user.lower() == "y" else 2
# password = ''.join(random.sample(zipped, passlen))
password = ''.join(random.choice(zipped) for i in range(passlen))
print(password)