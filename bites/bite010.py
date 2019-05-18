def positive_divide(numerator, denominator):
    try:
        frac = numerator / denominator
    except ZeroDivisionError:
        return 0
    except TypeError:
        raise TypeError("wrong type sis")
    else:
        if frac < 0:
            raise ValueError("why negative sis?")
        return frac