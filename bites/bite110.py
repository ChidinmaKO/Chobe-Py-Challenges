def divide_numbers(numerator, denominator):
    # First you try to convert them to ints, 
    # if that raises a ValueError you will 
    # re-raise it (using raise).
    try:
        num = int(numerator)
        den = int(denominator)
    except ValueError:
        raise ValueError("Can't be converted to an integer")
    else:
        try:
            frac = num / den
        except ZeroDivisionError:
            return 0
    return frac