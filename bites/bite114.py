import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
tmp = os.getenv("TMP", "/tmp")
color_values_module = os.path.join(tmp, 'color_values.py')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/color_values.py',
    color_values_module
)
sys.path.append(tmp)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self.color = color
        self.rgb = COLOR_NAMES.get(self.color.upper())

    @staticmethod
    def hex2rgb(value):
        """Static method that converts a hex value into an rgb one"""
        if len(value) != 7 or value[0] != '#':
            raise ValueError('Not a Hex value!')
        else:
            hex_ = value.lstrip('#')
            len_ = len(hex_)
            return tuple(int(hex_[i:i+int(len_/3)], 16) for i in range(0, len_, int(len_/3)))

        

    @staticmethod
    def rgb2hex(value):
        """Static method that converts an rgb value into a hex one"""
        try:
            if not all(0 <= i <= 255 for i in value):
                raise ValueError('Not in range!')
            return '#' + ''.join([f'{i:02x}' for i in value])
        except:
            raise ValueError('Not valid!')
        
        # hash_ = '#'
        # if len(value) != 3 or type(value) == str:
        #     raise ValueError("Not rgb!")
            
        # for i in value:
        #     if not i in range(0, 256):
        #         raise ValueError('Not in range!')
        #     else:
        #         hash_ += f"{i:02x}"
        #         return hash_

    def __repr__(self):
        """Returns the repl of the object"""
        return f"{self.__class__.__name__}('{self.color}')"

    def __str__(self):
        """Returns the string value of the color object"""
        return f"{self.rgb}" if self.color.upper() in COLOR_NAMES.keys() else "Unknown" 


# tests
import pytest

from color import Color


@pytest.mark.parametrize("color, expected", [
    ("white", (255, 255, 255)),
    ("black", (0, 0, 0)),
    ("blue", (0, 0, 255)),
    ("red", (255, 0, 0)),
    ("green", (0, 128, 0)),
    ("orange", (255, 128, 0)),
    ("puke", None),
])
def test_color_class(color, expected):
    c = Color(color)
    assert c.rgb == expected


@pytest.mark.parametrize("rgb, expected", [
    ((255, 255, 255), "#ffffff"),
    ((0, 0, 0), "#000000"),
    ((0, 0, 255), "#0000ff"),
    ((255, 0, 0), "#ff0000"),
    ((0, 128, 0), "#008000"),
    ((255, 128, 0), "#ff8000"),
])
def test_color_staticmethod_rgb2hex(rgb, expected):
    assert Color.rgb2hex(rgb) == expected


@pytest.mark.parametrize("rgb", [
    ("puke"),
    ("0, 0, 0"),
    ((0, -5, 255)),
    ((256, 0, 0)),
])

def test_color_rgb2hex_bad_value(rgb):
    with pytest.raises(ValueError):
        Color.rgb2hex(rgb)


@pytest.mark.parametrize("hex, expected", [
    ("#ffffff", (255, 255, 255)),
    ("#000000", (0, 0, 0)),
    ("#0000ff", (0, 0, 255)),
    ("#ff0000", (255, 0, 0)),
    ("#008000", (0, 128, 0)),
    ("#ff8000", (255, 128, 0)),
])
def test_color_staticmethod_hex2rgb(hex, expected):
    assert Color.hex2rgb(hex) == expected


@pytest.mark.parametrize("value", [
    ("puke"),
    ("#ccc"),
    ("#stopit"),
    ("pink"),
])
def test_color_hex2rgb_bad_value(value):
    with pytest.raises(ValueError):
        Color.hex2rgb(value)


def test_color_string_output():
    color = Color("brown")
    assert str(color) == "(165, 42, 42)"


def test_color_repr_output():
    color = Color("brown")
    assert repr(color) == "Color('brown')"


def test_unknown_color():
    color = Color("puke green")
    assert str(color) == "Unknown"