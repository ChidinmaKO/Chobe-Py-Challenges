import operator

operators = { '*': operator.mul, '/': operator.truediv, '+': operator.add, '-': operator.sub }

# shorter way

def simple_calculator(calculation):
    """Receives 'calculation' and returns the calculated result,

      Examples - input -> output:
      '2 * 3' -> 6
      '2 + 6' -> 8

      Support +, -, * and /, use "true" division (so 2/3 is .66
      rather than 0)

      Make sure you convert both numbers to ints.
      If bad data is passed in, raise a ValueError.
    """
    try:
        num1, op, num2 = calculation.split()
        operation = operators[op](int(num1), int(num2))
    except Exception:
        raise ValueError('Something\'s wrong')
    return operation

    
# another way

# def simple_calculator(calculation):
#     """Receives 'calculation' and returns the calculated result,

#       Examples - input -> output:
#       '2 * 3' -> 6
#       '2 + 6' -> 8

#       Support +, -, * and /, use "true" division (so 2/3 is .66
#       rather than 0)

#       Make sure you convert both numbers to ints.
#       If bad data is passed in, raise a ValueError.
#     """
    
    # operators = '+-*/'
    # num1, op, num2 = calculation.split()

    # num1 = int(num1)
    # num2 = int(num2)
    # if op not in operators:
    #   raise ValueError("Not an allowed operator")
    
    # try:
    #     if op == '*':
    #       return(num1 * num2)
    #     elif op == '/':
    #       return(num1 / num2)
    #     elif op == '+':
    #       return(num1 + num2)
    #     elif op == '-':
    #       return(num1 - num2)
    # except Exception:
    #     raise ValueError('exception')
    


# tests

import pytest

# from calculator import simple_calculator


@pytest.mark.parametrize("arg, expected", [
    ('2 + 3', 5),
    ('5 + 11', 16),
    ('12 + 18', 30),
])
def test_sum(arg, expected):
    assert simple_calculator(arg) == expected


@pytest.mark.parametrize("arg, expected", [
    ('3 - 2', 1),
    ('16 - 11', 5),
    ('12 - 18', -6),
])
def test_subtract(arg, expected):
    assert simple_calculator(arg) == expected


@pytest.mark.parametrize("arg, expected", [
    ('2 * 3', 6),
    ('-5 * -11', 55),
    ('3 * -6', -18),
])
def test_multiply(arg, expected):
    assert simple_calculator(arg) == expected


@pytest.mark.parametrize("arg, expected", [
    ('2 / 3', 0.67),
    ('1 / 5', 0.2),
    ('-2 / 175', -0.01),
])
def test_true_division(arg, expected):
    assert round(simple_calculator(arg), 2) == expected


@pytest.mark.parametrize("arg", [
    'a / 3', '2 / b', 'c / d', '1 2 3', '1 ^ 2',
    '1 x 2', 'some random string', '1 / 0',
    'really_bad_data'
])
def test_bad_inputs(arg):
    with pytest.raises(ValueError):
        simple_calculator(arg)