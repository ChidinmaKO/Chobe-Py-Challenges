def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    if not (type(value) == float or type(value) == int):
        raise TypeError("Wrong type, lady!")
    if fmt.lower() == "cm":
        result = value * 2.54
        return round(result, 4)
    if fmt.lower() == "in":
        result = value / 2.54
        return round(result, 4)
    else:
        raise ValueError("Wrong value, sis!")