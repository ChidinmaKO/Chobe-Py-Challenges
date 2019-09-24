import argparse


def calc_bmi(weight, length):
    """Provided/DONE:
       Calc BMI give a weight in kg and length in cm, return the BMI
       rounded on 2 decimals"""
    bmi = int(weight) / ((int(length) / 100) ** 2)
    return round(bmi, 2)


def create_parser():
    """TODO:
    Create an ArgumentParser adding the right arguments to pass the tests,
    returns a argparse.ArgumentParser object"""
    parser = argparse.ArgumentParser(description='Calculate BMI')
    parser.add_argument('-w', '--weight', type=int, help='Your weight in kg')
    parser.add_argument('-l', '--length', type=int, help='Your length in cm')
    return parser


def handle_args(args=None):
    """Provided/DONE:
       Call calc_bmi with provided args object.
       If args are not provided get them from create_parser"""
    if args is None:
        parser = create_parser()
        args = parser.parse_args()

    if args.weight and args.length:
        bmi = calc_bmi(args.weight, args.length)
        print(f'Your BMI is: {bmi}')
    else:
        # could enforce SystemExit in create_parser/add_argument, but argparse
        # docs are not clear how to do it, so raising the exception here manually
        raise SystemExit


if __name__ == '__main__':
    handle_args()


# tests
import pytest

# from bmi import create_parser, handle_args


@pytest.fixture
def parser():
    return create_parser()


def test_no_args_exits(parser):
    # parser.parse_args should raise the exception but in case
    # you raised it explicitly further down the stack let's check
    # if handle_args raises it (same applies to next test)
    with pytest.raises(SystemExit):
        handle_args()


def test_help_flag_exits(parser):
    with pytest.raises(SystemExit):
        args = parser.parse_args(['-h'])
        handle_args(args)


def test_only_width_exits(parser):
    with pytest.raises(SystemExit):
        args = parser.parse_args(['-w', '80'])
        handle_args(args)


def test_only_length_exits(parser):
    with pytest.raises(SystemExit):
        args = parser.parse_args(['-l', '187'])
        handle_args(args)


def test_two_arg(parser, capfd):
    args = parser.parse_args(['-w', '80', '-l', '187'])
    handle_args(args)
    output = capfd.readouterr()[0]
    assert "Your BMI is: 22.88" in output


def test_two_arg_reversed_order(parser, capfd):
    args = parser.parse_args(['-l', '187', '-w', '80'])
    handle_args(args)
    output = capfd.readouterr()[0]
    assert "Your BMI is: 22.88" in output


def test_different_args(parser, capfd):
    args = parser.parse_args(['-l', '200', '-w', '100'])
    handle_args(args)
    output = capfd.readouterr()[0]
    assert "Your BMI is: 25.0" in output