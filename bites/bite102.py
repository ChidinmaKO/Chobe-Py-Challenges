VALID_COLORS = ['blue', 'yellow', 'red']

def print_colors():
    while True:
        user_color = str(input("Please enter a color: "))
        user_color = user_color.lower()
        if user_color == 'quit':
            print('bye')
            break
        elif user_color not in VALID_COLORS:
            print('Not a valid color')
            continue
        else:
          print(user_color)
        pass