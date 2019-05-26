from secrets import choice
# secrets is preferred to random because it generates cryptographically secure 
# random numbers. Available from >= python 3.6

from string import ascii_uppercase, digits

def gen_key(parts=4, chars_per_part=8):
    items = ascii_uppercase + digits
    key = []
    
    for _ in range(parts):
        key.append(''.join(choice(items) for i in range(chars_per_part)))
        result = '-'.join(key)
    return result